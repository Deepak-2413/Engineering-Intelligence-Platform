import ast

IGNORED_NAMES = {
    "int",
    "str",
    "bool",
    "dict",
    "list",
    "set",
    "tuple",
    "len",
    "open",
    "isinstance",
    "issubclass",
    "TypeError",
    "ValueError",
    "RuntimeError",
    "NotImplementedError",
    "super",
    "getattr",
    "setattr",
    "iter",
    "next",
    "append",
    "extend",
    "update",
    "copy",
    "get",
    "setdefault",
    "pop",
    "items",
    "values",
    "keys",
    "join",
    "split",
    "partition",
    "rpartition",
    "startswith",
    "endswith",
    "lower",
    "upper",
    "strip",
    "lstrip",
    "rstrip",
    "read",
    "write",
    "close",
    "clear",
    "insert",
    "remove",
    "decode",
    "encode",
    "loads",
    "dumps",
    "warn",
    "cast"
}

class DependencyVisitor(ast.NodeVisitor):

    def __init__(self):
        self.current_class = None
        self.relationships = []

    def visit_ClassDef(self, node):

        previous_class = self.current_class
        self.current_class = node.name

        self.generic_visit(node)

        self.current_class = previous_class

    def visit_Call(self, node):

        if self.current_class:

            if isinstance(node.func, ast.Name):

                dependency = node.func.id

                if dependency not in IGNORED_NAMES:

                    self.relationships.append(
                        (self.current_class, dependency)
                    )

            elif isinstance(node.func, ast.Attribute):

                dependency = node.func.attr

                if dependency not in IGNORED_NAMES:

                    self.relationships.append(
                        (self.current_class, dependency)
                    )

        self.generic_visit(node)


class PythonParser:

    def parse_file(self, file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source_code = file.read()

        tree = ast.parse(source_code)

        visitor = DependencyVisitor()
        visitor.visit(tree)

        result = {
            "classes": [],
            "functions": [],
            "imports": [],
            "relationships": visitor.relationships
        }

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                result["classes"].append(node.name)

            elif isinstance(node, ast.FunctionDef):
                result["functions"].append(node.name)

            elif isinstance(node, ast.Import):

                for alias in node.names:
                    result["imports"].append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    result["imports"].append(
                        node.module
                    )

        return result
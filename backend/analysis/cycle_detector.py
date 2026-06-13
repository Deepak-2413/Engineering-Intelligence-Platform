class CycleDetector:

    def detect_cycles(self, graph):

        visited = set()
        recursion_stack = set()

        def dfs(node):

            visited.add(node)
            recursion_stack.add(node)

            for neighbor in graph.get(node, []):

                if neighbor not in visited:

                    if dfs(neighbor):
                        return True

                elif neighbor in recursion_stack:
                    return True

            recursion_stack.remove(node)

            return False

        for node in graph:

            if node not in visited:

                if dfs(node):
                    return True

        return False
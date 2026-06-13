class SecurityScanner:

    def scan(self, graph):

        findings = []

        dangerous_patterns = [
            "eval",
            "exec",
            "pickle.loads",
            "shell=True"
        ]

        for component, dependencies in graph.items():

            for dependency in dependencies:

                for pattern in dangerous_patterns:

                    if pattern in str(dependency):

                        findings.append({
                            "component": component,
                            "risk": pattern
                        })

        return findings
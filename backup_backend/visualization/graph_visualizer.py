from pyvis.network import Network


class GraphVisualizer:

    def generate_graph(
        self,
        graph,
        output_file="repository_graph.html"
    ):

        net = Network(
            height="750px",
            width="100%",
            directed=True
        )

        for source, targets in graph.items():

            net.add_node(
                source,
                label=source
            )

            for target in targets:

                net.add_node(
                    target,
                    label=target
                )

                net.add_edge(
                    source,
                    target
                )

        net.save_graph(
            output_file
        )

        return output_file
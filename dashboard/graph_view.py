from streamlit_agraph import (
    agraph,
    Node,
    Edge,
    Config
)

import streamlit as st


def show_graph(graph, critical_components):

    if not graph:
        st.warning("No graph data found")
        return

    critical_names = [
        component[0]
        for component in critical_components
    ]

    nodes = []
    edges = []

    added = set()

    # limit huge graphs
    max_nodes = 150

    for source, targets in list(graph.items())[:max_nodes]:

        if source not in added:

            nodes.append(
                Node(
                    id=str(source),
                    label=str(source),
                    size=25,
                    color="red"
                    if source in critical_names
                    else "skyblue"
                )
            )

            added.add(source)

        for target in targets[:10]:

            if target not in added:

                nodes.append(
                    Node(
                        id=str(target),
                        label=str(target),
                        size=15,
                        color="red"
                        if target in critical_names
                        else "lightgreen"
                    )
                )

                added.add(target)

            edges.append(
                Edge(
                    source=str(source),
                    target=str(target)
                )
            )

    st.write(
        f"Nodes: {len(nodes)} | Edges: {len(edges)}"
    )

    config = Config(
        width=1400,
        height=800,
        directed=True,
        physics=True,
        hierarchical=False,
        nodeHighlightBehavior=True,
        highlightColor="#F7A7A6",
        collapsible=True
    )

    agraph(
        nodes=nodes,
        edges=edges,
        config=config
    )
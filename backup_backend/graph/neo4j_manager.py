from neo4j import GraphDatabase


class Neo4jManager:

    def __init__(self, uri, username, password):

        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

    def close(self):
        self.driver.close()

    def clear_database(self):

        query = """
        MATCH (n)
        DETACH DELETE n
        """

        with self.driver.session() as session:
            session.run(query)

    def create_class_node(self, class_name):

        query = """
        MERGE (c:Class {name: $name})
        """

        with self.driver.session() as session:
            session.run(query, name=class_name)

    def create_dependency(self, source, target):

        query = """
        MERGE (a:Class {name: $source})
        MERGE (b:Class {name: $target})

        MERGE (a)-[:DEPENDS_ON]->(b)
        """

        with self.driver.session() as session:
            session.run(
                query,
                source=source,
                target=target
            )

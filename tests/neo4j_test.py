from backend.graph.neo4j_manager import Neo4jManager

URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ynvdeepak@24"


db = Neo4jManager(
    URI,
    USERNAME,
    PASSWORD
)

db.create_class_node("UserService")

print("Connection Successful")

db.close()
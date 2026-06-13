from backend.graph.neo4j_manager import Neo4jManager


URI = "bolt://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ynvdeepak@24"


db = Neo4jManager(
    URI,
    USERNAME,
    PASSWORD
)

db.clear_database()

db.create_dependency(
    "AuthService",
    "UserService"
)

db.create_dependency(
    "PaymentService",
    "AuthService"
)

print("Graph Loaded Successfully")

db.close()
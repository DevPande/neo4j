from neo4j import GraphDatabase, basic_auth

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "pict@1999"), encrypted=False)

session = driver.session()
cqlCreate = 'CREATE (Devdatta:student{name: "Devdatta", YOB: 1999, POB: "Pune"})' \
            'CREATE (BinaryDots:company{name: "BinaryDots"})' \
            'CREATE (RD:department{name: "R&D"})' \
            'CREATE (HR:department{name: "HR"})' \
            'CREATE (Finance:department{name: "Finance"})' \
            'CREATE (Web:department{name: "Web"})' \
            'CREATE (node1:friend{name: "node1", YOB: 1999, POB: "Delhi"})' \
            'CREATE (node2:friend{name: "node2", YOB: 1985, POB: "Mumbai"})' \
            'CREATE (node3:friend{name: "node3", YOB: 1997, POB: "Delhi"})' \
            'CREATE (node4:friend{name: "node4", YOB: 1985, POB: "Delhi"})' \
            'CREATE (node5:friend{name: "node5", YOB: 1993, POB: "Pune"})' \
            'CREATE (Deep:department{name: "Deep Learning"})'
session.run(cqlCreate)

def createDeptRelation(name):
    cqlRelateDept2 = "MATCH (a:company), (b:department) WHERE a.name = 'BinaryDots' AND b.name = " + name + "\n" + "CREATE (a)-[r: HAS_DEPT]->(b)"

    session.run(cqlRelateDept2)



def createFriendRelation(name):
    cqlRelateFriend2 = "MATCH (a:student), (b:friend) WHERE a.name = 'Devdatta' AND b.name = " + name + "\n" + "CREATE (a)-[r: FRIEND_OF]->(b)"

    session.run(cqlRelateFriend2)


createDeptRelation("'R&D'")
createDeptRelation("'Deep Learning'")
createDeptRelation("'Web'")
createDeptRelation("'Finance'")
createDeptRelation("'HR'")

createDeptRelation("'node1'")
createDeptRelation("'node2'")
createDeptRelation("'node3'")
createDeptRelation("'node4'")
createDeptRelation("'node5'")


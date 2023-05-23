from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:2020/sparql")
sparql.setQuery("""
    SELECT * 
    WHERE {
        ?s ?p ?o .
    }
    LIMIT 10
""")
# sparql.setQuery("""
#     SELECT DISTINCT ?o
#     WHERE {
#         ?s
#         <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o.} LIMIT 10
#         """)
# sparql.setQuery("""
#     SELECT DISTINCT *
#     WHERE {
#         ?s
#         <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://localhost:2020/resource/vocab/hotel> .}
#         """)
# sparql.setQuery("""
#     SELECT DISTINCT *
#     WHERE {
#         ?s
#         <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://localhost:2020/resource/vocab/heritage> .}
#         """)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(len(results))
print(len(results["results"]["bindings"]))
# print(results)
for result in results["results"]["bindings"]:
    print(result["s"]["value"], result["p"]["value"], result["o"]["value"], )
    # print(result["s"]["value"], result["o"]["value"], )
    # print(result["o"]["value"], )
    # print(result["s"]["value"], )

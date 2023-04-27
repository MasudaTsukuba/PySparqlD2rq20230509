from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:2020/sparql")
sparql.setQuery("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab: <http://localhost:2020/resource/vocab/>
SELECT ?name 
WHERE {
    <http://localhost:2020/resource/hotel/1585008h>
    vocab:name ?name.
}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(len(results))
print(len(results["results"]["bindings"]))
# print(results)
for result in results["results"]["bindings"]:
    print(result["name"]["value"])

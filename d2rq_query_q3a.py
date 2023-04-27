from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:2020/sparql")
sparql.setQuery("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab: <http://localhost:2020/resource/vocab/>
SELECT ?s ?name ?cname
WHERE {
    ?s vocab:name ?name;
    vocab:place_in ?c_id.
    ?c_id vocab:country_name ?cname.
    FILTER(?cname = 'United Kingdom')
}""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(len(results))
print(len(results["results"]["bindings"]))
# print(results)
# for result in results["results"]["bindings"]:
#     print(result["s"]["value"], ';', result["name"]["value"], ';', result["cname"]["value"])

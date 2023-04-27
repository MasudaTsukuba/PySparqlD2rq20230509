from SPARQLWrapper import SPARQLWrapper, JSON
from uri_trans import uri2str, str2uri
import csv
import replace_prefix

sparql = SPARQLWrapper("http://localhost:2020/sparql")
file = 'q7.csv'
my_query = """
SELECT ?name 
WHERE {
    <http://localhost:2020/resource/hotel/1585008h> <http://www.w3.org/1999/02/22-rdf-syntax-ns#label> ?name.
} 
"""
# str_query = uri2str(my_query)
# print(str_query)

my_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ontology/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?name
WHERE {
    <http://example.com/hotel/id/1585008h> rdf:label ?name.
}"""
replaced_query = replace_prefix.replace_prefix(my_query)
str_query = uri2str(replaced_query)
print(str_query)

sparql.setQuery(str_query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(len(results))
print(len(results["results"]["bindings"]))
# print(results)
outputs = [['name']]
for result in results["results"]["bindings"]:
    # print(str2uri(result["s"]["value"]), ';', str2uri(result["name"]["value"]), ';', str2uri(result["cname"]["value"]))
    outputs.append([str2uri(result["name"]["value"])])
with open('output/'+file, 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(outputs)

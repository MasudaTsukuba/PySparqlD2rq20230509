from SPARQLWrapper import SPARQLWrapper, JSON
from uri_trans import uri2str, str2uri
import csv
import replace_prefix

file = 'q3b.csv'
sparql = SPARQLWrapper("http://localhost:2020/sparql")
my_query = """
SELECT distinct ?name ?cname
WHERE {
    ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#label> ?name.
    ?s <http://example.com/predicate/country> ?c_id.
    ?c_id <http://example.com/predicate/country_name> ?cname.
    FILTER(?cname = 'United Kingdom')
} 
"""
my_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ontology/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT distinct ?name ?cname
WHERE {
    ?s rdf:label ?name.
    ?s country: ?c_id.
    ?c_id country_name: ?cname.
    FILTER(?cname = 'United Kingdom')
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
outputs = [['name', 'cname']]
for result in results["results"]["bindings"]:
    outputs.append([str2uri(result["name"]["value"]), str2uri(result["cname"]["value"])])
with open('output/'+file, 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(outputs)

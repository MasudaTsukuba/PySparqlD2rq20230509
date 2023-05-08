import ast
import json
import re

import rdflib.plugins.sparql.parser

sparql_string = 'SELECT ?s  WHERE {?s <http://foaf/friend> ?o ; <http://foaf/name> ?name.} LIMIT 10'

str_dict = {'<http://foaf/friend>': '<http://example.com/friend>', '<http://foaf/name>': '<http://example.com/name>'}

matches = re.findall(r'<(.*?)>', sparql_string)
for match in matches:
    sparql_string = sparql_string.replace(f'<{match}>', str_dict[f'<{match}>'])
# print(sparql_string)
pass

query_input = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ontology/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?s ?name ?cname
WHERE {
    ?s rdf:type ex:Hotel.
    ?s rdf:label ?name.
    ?s country: ?c_id.
    ?c_id country_name: ?cname.
}
"""
prefix = 'rdf'
uri = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
pattern = re.compile(fr'{prefix}:(\w*)')
query_output = pattern.sub(f'<{uri}\\1>', query_input)  # \\1 is (\w*)
pattern = re.compile(fr'{prefix}:(..)([a-z:A-Z]*)')
query_output = pattern.sub(f'<{uri}\\2\\1>', query_input)  # \\1 is (\w*)
# print(query_output)

parsed_query = rdflib.plugins.sparql.parser.parseQuery(query_input)
xxx = str(parsed_query)
print(xxx)
# yyy = ast.literal_eval(xxx)
print(json.loads(xxx))
for p in parsed_query[0]:
    print(p.name)
print(parsed_query[1].name)
print(parsed_query[1].values())
for x in parsed_query[1].values():
    print(x)


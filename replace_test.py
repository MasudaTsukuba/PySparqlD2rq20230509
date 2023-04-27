import re

sparql_string = 'SELECT ?s  WHERE {?s <http://foaf/friend> ?o ; <http://foaf/name> ?name.} LIMIT 10'

str_dict = {'<http://foaf/friend>': '<http://example.com/friend>', '<http://foaf/name>': '<http://example.com/name>'}

matches = re.findall(r'<(.*?)>', sparql_string)
for match in matches:
    sparql_string = sparql_string.replace(f'<{match}>', str_dict[f'<{match}>'])
print(sparql_string)
pass

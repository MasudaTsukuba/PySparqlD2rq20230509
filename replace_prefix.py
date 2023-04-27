import re
from rdflib.plugins.sparql.parser import parseQuery


def replace_prefix(sparql_query):
    return_query = sparql_query
    parsed_query = parseQuery(sparql_query)
    prefixes = {}
    prefix_items = parsed_query.as_list()[0]
    for decl in prefix_items:
        prefix_string = decl['prefix']
        iri_string = decl['iri']
        prefixes[prefix_string] = str(iri_string)
        pass

    pattern = r'PREFIX (.*?)>(.*?)\n'
    return_query = re.sub(pattern, '', return_query)
    # pattern = r'(\n\n)'
    # for i in range(10):
    #     return_query = re.sub(pattern, '\n', return_query)

    for prefix, uri in prefixes.items():
        pattern = re.compile(fr'{prefix}:(\w*)')
        return_query = pattern.sub(f'<{uri}\\1>', return_query)
    return return_query


if __name__ == '__main__':
    query = """
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
    replaced_query = replace_prefix(query)
    print(replaced_query)

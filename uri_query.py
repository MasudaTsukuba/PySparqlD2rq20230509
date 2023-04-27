import ast

from SPARQLWrapper import SPARQLWrapper, JSON
from uri_trans import uri2str, str2uri
import csv
import replace_prefix


def uri_query(query, header, file):
    print(file)
    sparql = SPARQLWrapper("http://localhost:2020/sparql")
    replaced_query = replace_prefix.replace_prefix(query)
    str_query = uri2str(replaced_query)
    print(str_query)

    sparql.setQuery(str_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(len(results))
    print(len(results["results"]["bindings"]))
    outputs = [header]
    result_string = str(results["results"]["bindings"])
    print('start uri')  # debug
    replaced_string = str2uri(result_string)
    print('end uri')  # debug
    results_list = ast.literal_eval(replaced_string)
    # for result in results["results"]["bindings"]:
    print('start packing')  # debug
    for result in results_list:
        row = []
        for var in header:
            # row.append(str2uri(result[var]["value"]))
            row.append(result[var]["value"])
        outputs.append(row)
    print('end packing')  # debug
    with open('output/'+file, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(outputs)


if __name__ == '__main__':
    query_q1 = """
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
    file_q1 = 'q1.csv'
    header_q1 = ['s', 'name', 'cname']
    uri_query(query_q1, header_q1, file_q1)

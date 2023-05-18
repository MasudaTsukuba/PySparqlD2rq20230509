import ast

from SPARQLWrapper import SPARQLWrapper, JSON
from uri_trans import uri2str, str2uri
import csv
import replace_prefix


def execute_query(input_file):
    pass
    query = ''
    path = '/home/masuda/PycharmProjects/PySparqlQuery20230508/'
    with open(path+input_file, 'r') as f:
        query = f.read()
    temp1 = query.split('SELECT ')
    temp2 = temp1[1].split('WHERE')
    header = temp2[0].replace('distinct ', '').replace('\n', '').replace('?', '').split(' ')
    file = input_file.replace('query/', '').replace('.txt', '.csv')
    results = uri_query(query, header, file)
    return results['results']['bindings']


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
    output_temp = []
    for result in results_list:
        row = []
        for var in header:
            # row.append(str2uri(result[var]["value"]))
            row.append(result[var]["value"])
        output_temp.append(row)
    sorted_outputs = sorted(output_temp, key=lambda x: x[0])
    for row in sorted_outputs:
        outputs.append(row)
    print('end packing')  # debug
    with open('output/'+file, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(outputs)
    return results


if __name__ == '__main__':
    execute_query('query/q1.txt')
    # execute_query('query/q3b.txt')
    # execute_query('query/q1pred_hotel.txt')

    # query_q1 = """
    # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    # PREFIX ex: <http://example.com/ontology/>
    # PREFIX country: <http://example.com/predicate/country>
    # PREFIX country_name: <http://example.com/predicate/country_name>
    # PREFIX country_comment: <http://example.com/predicate/country_comment>
    #
    # SELECT ?s ?name ?cname
    # WHERE {
    #     ?s rdf:type ex:Hotel.
    #     ?s rdf:label ?name.
    #     ?s country: ?c_id.
    #     ?c_id country_name: ?cname.
    # }
    # """
    # file_q1 = 'q1.csv'
    # header_q1 = ['s', 'name', 'cname']
    # uri_query(query_q1, header_q1, file_q1)

    # query_q1 = """
    # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    # PREFIX ex: <http://example.com/ontology/>
    # PREFIX country: <http://example.com/predicate/country>
    # PREFIX country_name: <http://example.com/predicate/country_name>
    # PREFIX country_comment: <http://example.com/predicate/country_comment>
    #
    # SELECT DISTINCT ?o
    # WHERE {
    #     ?s rdf:type ?o.
    # } LIMIT 10
    # """
    # file_q1 = 'test.csv'
    # header_q1 = [  'o']
    # uri_query(query_q1, header_q1, file_q1)

from SPARQLWrapper import SPARQLWrapper, JSON
from uri_trans import uri2str, str2uri
import csv
import ast
import os
import replace_prefix

current_working_dir = os.getcwd()
working_dir = current_working_dir
if working_dir.endswith('src'):
    working_dir = os.path.dirname(working_dir)
# temp = os.listdir(working_dir)
common_query_path = os.path.dirname(working_dir)+'/PySparqlQuery20230508/query/'


def execute_query(input_file):
    pass
    sparql_query = ''
    # path = '/home/masuda/PycharmProjects/PySparqlQuery20230508/'
    with open(common_query_path+input_file, 'r') as f:
        sparql_query = f.read()
    temp1 = sparql_query.split('SELECT ')
    temp2 = temp1[1].split('WHERE')
    header = temp2[0].replace('distinct ', '').replace('\n', '').replace('?', '').split(' ')
    output_file = input_file.replace('.txt', '.csv')  # output file name
    results = uri_query(sparql_query, header, output_file)
    return results['results']['bindings']


def uri_query(sparql_query, header, file):
    print(file)

    # preparing for query
    sparql = SPARQLWrapper("http://localhost:2020/sparql")
    replaced_query = replace_prefix.replace_prefix(sparql_query)
    str_query = uri2str(replaced_query)
    print(str_query)
    sparql.setQuery(str_query)
    sparql.setReturnFormat(JSON)

    # start query against d2rq
    results = sparql.query().convert()  # query against a sparql end point
    print(len(results["results"]["bindings"]))  # debug
    outputs = [header]
    result_string = str(results["results"]["bindings"])
    print('start uri')  # debug
    replaced_string = str2uri(result_string)
    print('end uri')  # debug

    # save the results in a csv file
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
    sorted_outputs = sorted(output_temp, key=lambda x: (x[0]))  # sort the results
    for row in sorted_outputs:
        outputs.append(row)
    print('end packing')  # debug
    with open(working_dir+'/output/'+file, 'w') as file:  # write to a csv file
        csv_writer = csv.writer(file)
        csv_writer.writerows(outputs)
    return results


if __name__ == '__main__':
    query = 'q1.txt'
    query = 'q3b.txt'
    query = 'q5.txt'
    query = 'q1pred_build.txt'
    query = 'query_type_object_hotel20230518.txt'
    # query = 'q1pred_get_hotel.txt'
    execute_query(query)

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

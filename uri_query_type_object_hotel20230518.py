from SPARQLWrapper import SPARQLWrapper, JSON
from uri_trans import uri2str, str2uri
import csv
import replace_prefix
from uri_query import uri_query


common_query_path = '/home/masuda/PycharmProjects/PySparqlQuery20230508/query/'

if __name__ == '__main__':
    input_file = 'query_type_object_hotel20230518.txt'
    with open(common_query_path+input_file, 'r') as output_file:
        query = output_file.read()
    # query = """
    # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    # PREFIX ex: <http://example.com/ontology/>
    # PREFIX country: <http://example.com/predicate/country>
    # PREFIX country_name: <http://example.com/predicate/country_name>
    # PREFIX country_comment: <http://example.com/predicate/country_comment>
    #
    # SELECT ?s ?name ?cname
    # WHERE {
    #     ?s rdf:type ex:Museum.
    #     ?s rdf:label ?name.
    #     ?s country: ?c_id.
    #     ?c_id country_name: ?cname.
    #     FILTER(?cname = 'United Kingdom')
    # }    """
    output_file = input_file.replace('.txt', '.csv')
    header = ['s', 'type']
    uri_query(query, header, output_file)



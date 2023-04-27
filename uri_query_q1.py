from SPARQLWrapper import SPARQLWrapper, JSON
from uri_trans import uri2str, str2uri
import csv
import replace_prefix
from uri_query import uri_query


def uri_query_q1():
    file = 'q1.csv'
    sparql = SPARQLWrapper("http://localhost:2020/sparql")
    my_query = """
    SELECT ?s ?name ?cname
    WHERE {
        ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/hotel>.
        ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#label> ?name.
        ?s <http://example.com/predicate/country> ?c_id.
        ?c_id <http://example.com/predicate/country_name> ?cname.
    } 
    """
    my_query = """
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
    replaced_query = replace_prefix.replace_prefix(my_query)
    str_query = uri2str(replaced_query)
    print(str_query)

    sparql.setQuery(str_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(len(results))
    print(len(results["results"]["bindings"]))
    # print(results)
    outputs = [['s', 'name', 'cname']]
    for result in results["results"]["bindings"]:
        # print(str2uri(result["s"]["value"]), ';', str2uri(result["name"]["value"]), ';', str2uri(result["cname"]["value"]))
        outputs.append([str2uri(result["s"]["value"]), str2uri(result["name"]["value"]), str2uri(result["cname"]["value"])])
    with open('output/'+file, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(outputs)


if __name__ == '__main__':
    # uri_query_q1()
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

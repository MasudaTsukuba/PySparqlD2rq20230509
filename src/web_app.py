from flask import Flask, request
from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import html

sparql = SPARQLWrapper("http://localhost:2020/sparql")

app = Flask(__name__)


def transform(input_string):
    response = requests.get(f'http://localhost:5001/?str2uri={input_string}')

    if response.status_code == 200:
        data = response.json()
        print(data['uri'])
        return data['uri']
    else:
        print('Error: ', response.status_code)
        return input_string


@app.route("/")
def hello():
    try:
        sparql_query = request.args.get("query")
        # sparql.setQuery("""
        #     SELECT *
        #     WHERE {
        #         ?s ?p ?o .
        #     }
        #     LIMIT 10
        # """)
        sparql.setQuery(sparql_query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return_string = str(len(results["results"]["bindings"]))+"<br><br>"
        print(len(results))
        print(results)
        for result in results["results"]["bindings"]:
            print(result["s"]["value"], result["p"]["value"], result["o"]["value"])
            subject_string = html.escape(transform(result["s"]["value"]))
            predicate_string = html.escape(transform(result["p"]["value"]))
            object_string = html.escape(transform(result["o"]["value"]))
            return_string += subject_string+"<br>"+predicate_string+"<br>"+object_string+"<br><br>"
        return return_string
    except TypeError:
        return "query was not given."


if __name__ == "__main__":
    app.run(port=5000)

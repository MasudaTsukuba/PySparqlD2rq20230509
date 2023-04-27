import os
from uri_query import uri_query


if __name__ == '__main__':
    target_files = ['q1.csv', 'q2.csv', 'q3a.csv', 'q3b.csv', 'q4.csv', 'q5.csv', 'q6.csv', 'q7.csv']
    headers = {'q1': ['s', 'name', 'cname'],
               'q2': ['s', 'name', 'cname'],
               'q3a': ['s', 'name', 'cname'],
               'q3b': ['name', 'cname'],
               'q4': ['s', 'name', 'cname'],
               'q5': ['s', 'name', 'cname'],
               'q6': ['s', 'name', 'cname'],
               'q7': ['name']}
    directory_path = 'query/'
    for query_file in os.listdir(directory_path):
        with open(directory_path+query_file, 'r') as f:
            query = f.read()
        print(query_file)
        file = query_file.replace('.txt', '.csv')
        header = headers[query_file.replace('.txt', '')]
        uri_query(query, header, file)

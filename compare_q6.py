import csv

file = 'q6.csv'
with open('output/'+file, 'r') as file1, open('/home/masuda/PycharmProjects/PythonSparqlSqlSatoNew20230327/output/'+file, 'r') as file2:
    reader1 = csv.reader(file1)
    rows1 = list(reader1)
    sorted_rows1 = sorted(rows1, key=lambda x: x[0])
    reader2 = csv.reader(file2)
    rows2 = list(reader2)
    sorted_rows2 = sorted(rows2, key=lambda x: x[0])
for row1, row2 in zip(sorted_rows1, sorted_rows2):
    if row1 != row2:
        print(row1, row2)
        print('##################')
        pass

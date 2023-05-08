import csv

target_file = 'q1pred_build.csv'


def compare_csv(file):
    with open('output/'+file, 'r') as file1, open('/home/masuda/PycharmProjects/PySparqlFuseki20230501/output/'+file, 'r') as file2:
        reader1 = csv.reader(file1)
        rows1 = list(reader1)
        sorted_rows1 = sorted(rows1, key=lambda x: x[0])
        reader2 = csv.reader(file2)
        rows2 = list(reader2)
        sorted_rows2 = sorted(rows2, key=lambda x: x[0])
    for row1, row2 in zip(sorted_rows1, sorted_rows2):
        row1_str = str(row1)
        row2_str = str(row2)
        row2_str = row2_str.replace('building/id', 'country/id')
        if row1_str != row2_str:
            print(row1_str, row2_str)
            print('##################')
            pass


if __name__ == '__main__':
    compare_csv(target_file)

import csv
import difflib

target_file = 'q5.csv'


def compare_csv(file):
    with open('output/'+file, 'r') as file1, open('/home/masuda/PycharmProjects/PythonSparqlSqlSatoNew20230327/output/'+file, 'r') as file2:
        differ = difflib.Differ()
        file1_lines = file1.readlines()
        file1_lines.sort()
        file2_lines = file2.readlines()
        file2_lines.sort()
        diff = list(differ.compare(file1_lines, file2_lines))
        count = 10
        for line in diff:
            if line.startswith('+') or line.startswith('-'):
                print(line)
                count -= 1
                if count == 0:
                    break

    #     reader1 = csv.reader(file1)
    #     rows1 = list(reader1)
    #     sorted_rows1 = sorted(rows1, key=lambda x: x[0])
    #     reader2 = csv.reader(file2)
    #     rows2 = list(reader2)
    #     sorted_rows2 = sorted(rows2, key=lambda x: x[0])
    # for row1, row2 in zip(sorted_rows1, sorted_rows2):
    #     if row1 != row2:
    #         print(row1, row2)
    #         print('##################')
    #         pass


if __name__ == '__main__':
    compare_csv(target_file)

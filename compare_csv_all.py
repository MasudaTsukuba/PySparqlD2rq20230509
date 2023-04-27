from compare_csv import compare_csv
import csv

target_files = ['q1.csv', 'q2.csv', 'q3a.csv', 'q3b.csv', 'q4.csv', 'q5.csv', 'q6.csv', 'q7.csv']


def compare_csv_all(files):
    for file in files:
        print(file)
        compare_csv(file)


if __name__ == '__main__':
    compare_csv_all(target_files)

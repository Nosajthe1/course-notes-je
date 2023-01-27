import csv

def open_csv(csv_file):
    with open(csv_file) as file_name:
        reader_obj = csv.reader(file_name)
        for row in reader_obj:
            print(row)


open_csv("user_details.csv")

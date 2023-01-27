import csv


def open_csv(csv_file):
    with open(csv_file) as file_name:
        reader_obj = csv.reader(file_name)
        new_list = []
        for row in reader_obj:
            # string = row[1], row[2], str.partition(row[4], "@")[0]
            new_list.append(row)
    return new_list


print(open_csv("user_details.csv"))


def transform_csv(file_name):
    user_details = open_csv(file_name)
    refined_user_list = []
    for details in user_details:
        refined_user_list.append(details[1] + " " + details[2] + " " + str.partition(details[4], '@')[0])
    return refined_user_list


print(transform_csv("user_details.csv"))


def write_csv(file_name):
    transformed_csv = transform_csv(file_name)
    transformed_split = []
    for line in transformed_csv:
        transformed_split.append(line.split(" "))

    with open('transformed_finished.csv', 'w', newline='') as user_select:
        details_writer = csv.writer(user_select)
        details_writer.writerows(transformed_split)


print(write_csv('user_details.csv'))

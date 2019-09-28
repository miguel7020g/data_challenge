import sys
import json


user_params = sys.argv[1:]
searched_value = user_params[0]
matrix = user_params[1]
column_indicator = int(user_params[2]) - 1

with open(matrix) as json_file:
    data = json.load(json_file)


def vlookup(searched_value, matrix_data, column_indicator):
    columns = list()
    for i in matrix_data.keys():
        columns.append(i)

    for j in matrix_data[columns[0]]:
        column_indicator_element = str(matrix_data[columns[0]][j])
        if searched_value == column_indicator_element:
            return(matrix_data[columns[column_indicator]][j])

print(vlookup(searched_value, data, column_indicator))

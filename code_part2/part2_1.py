import sys
user_data = sys.argv[1:]


def max_diff(data_array):
    try:
        data_array = list(map(float, data_array))
    except ValueError:
        return("Oops!  There is an invalid element.  Try again...")

    max_element = None
    min_element = None

    for item in data_array:
        if max_element == None:
            max_element = item
            min_element = item

        if item > max_element:
            max_element = item

        if item < min_element:
            min_element = item

    return max_element - min_element


print(max_diff(user_data))

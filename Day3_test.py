# convert dictionary to query string e.g. "abc=123&def=456&hij=789"
print() # to move cursor onto new line in test window

input_dict = {"abc": "123", "def": "456", "hij": "789"}


def convert_to_query_string(dict):
    query_list = []

    for key in dict:
        query_list.append(f"{key}={dict[key]}")

    return "&".join(query_list)

print(convert_to_query_string(input_dict))


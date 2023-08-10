def lookup_key(data, value):
    found_keys = []
    for key, val in data.items():
        if val == value:
            found_keys.append(key)
    return found_keys

my_dict = {
    "apple": "fruit",
    "banana": "fruit",
    "carrot": "vegetable",
    "grape": "fruit",
    "orange": "fruit",
    "potato": "vegetable"
}

value_to_search = "fruit"
result_keys = lookup_key(my_dict, value_to_search)
print("Знайдені ключі за значенням '{}':".format(value_to_search), result_keys)
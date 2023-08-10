def prepare_data(data):

    if len(data) <= 2:
        return data

    data_without_extremes = data.copy()
    data_without_extremes.remove(max(data_without_extremes))
    data_without_extremes.remove(min(data_without_extremes))

    data_without_extremes.sort()

    return data_without_extremes

data_list = [10, 5, 20, 15, 25, 30]
prepared_data = prepare_data(data_list)
print("Підготований список:", prepared_data)
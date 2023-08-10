points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    global points
    total_distance = 0.0
    for i in range(len(coordinates) - 1):
        start_point = coordinates[i]
        end_point = coordinates[i + 1]
        key = (start_point, end_point) if start_point < end_point else (end_point, start_point)
        total_distance += points[key]
    return total_distance


coordinates = [0, 1, 3, 2, 0]
total_distance = calculate_distance(coordinates)
print("Загальна відстань: ", total_distance)
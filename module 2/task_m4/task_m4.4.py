def get_grade(key):
        if key == "A" or key == "B":
            return 5
        elif key == "C":
            return 4
        elif key == "D" or key == "E":
            return 3
        elif key == "FX":
            return 2
        elif key == "F":
            return 1
        else:
            return None

def get_description(key):
    if key == "A":
        return "Perfectly"
    elif key == "B":
        return 'Very good'
    elif key == "C":
        return "Good"
    elif key == "D":
        return "Satisfactorily"
    elif key == "E":
        return "Enough"
    elif key == "FX" or key == "F":
        return "Unsatisfactorily"
    else:
        return None


print(get_grade(key="A"))
print(get_description(key="AA"))
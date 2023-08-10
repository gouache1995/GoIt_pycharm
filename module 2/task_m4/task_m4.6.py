def split_list(grade):
    if not grade:
        return [], []

    men_grade = []
    max_grade = []
    summa = sum(grade)
    avg_grade = summa / len(grade)

    for val in grade:
        if val <= avg_grade:
            max_grade.append(val)
        else:
            men_grade.append(val)

    return max_grade, men_grade



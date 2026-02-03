
def sum_grades(homework_grades):
    sum = 0
    for grade in homework_grades.values():
        sum += grade
    final_grade = sum / round((len(homework_grades) or 1), 2)
    print(final_grade)
    return final_grade

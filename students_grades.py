students = int(input())
dict_students = {}
for student in range(students):
    student, grades_str = input().split()
    grade = float(grades_str)

    if student not in dict_students.keys():
        dict_students[student] = []

    dict_students[student].append(grade)


def avg(values):
    return sum(values) / len(values)


for student, grades in dict_students.items():
    avg_grade = avg(grades)
    formatted_avg = f'{avg_grade:.2f}'
    formatted_grades = ' '.join(f'{grade:.2f}' for grade in grades)
    print(f'{student} -> {formatted_grades} (avg: {formatted_avg})')
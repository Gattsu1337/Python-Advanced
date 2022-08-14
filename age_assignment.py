def age_assignment(*args, **kwargs):
    people = {}
    for key, item in kwargs.items():
        for value in args:
            if value[0] == key:
                people[value] = item

    sorted_list = sorted(people)

    sorted_people = {}
    for person in sorted_list:
        sorted_people[person] = people[person]

    result = ''
    for key, item in sorted_people.items():
        result += f'{key} is {item} years old.\n'
    return result

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
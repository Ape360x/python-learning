students = [
    {"name": "Ada", "score": 78},
    {"name": "Bola", "score": 91},
    {"name": "Chidi", "score": 64},
    {"name": "Dayo", "score": 88},
]



def top_students(students):
    if not students:
        return None
    best_score = -1
    best_name = None
    for student in students:
        if student["score"] >= best_score:
            best_score = student["score"]
            best_name = student["name"]
    return best_name

def students_above(students, minimum=70):
    names = []
    for student in students:
        if student["score"] >= minimum:
            names.append(student["name"])
    return names

def count_above(students, minimum=70):
    return len(students_above(students, minimum))

def average_score(students):
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)




if __name__ == "__main__":
    print(top_students(students))
    print(top_students([]))
    print(students_above(students))
    print(students_above(students, 85))
    print(students_above(students, minimum=60))
    print(count_above(students, 85))
    print(average_score(students))
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




if __name__ == "__main__":
    print(top_students(students))
    print(top_students([]))
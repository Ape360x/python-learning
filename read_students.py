import json

from students import top_students

with open("data.json") as f:
    students = json.load(f)

print(students)

print(students["status"])

print(len(students["students"]))

print(top_students(students["students"]))

scores = []
for student in students["students"]:
    scores.append(student["score"])

print(sum(scores) / len(scores))
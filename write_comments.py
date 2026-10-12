import json
from groq_chat import ask

with open("data.json") as f:
    data = json.load(f)

results = []

for student in data["students"]:
    prompt = f"""You are a teacher writing a short comment for a student's report card.

Score: {student["score"]} out of 100
Subject: {student["subject"]}

Write exactly one sentence, no more than 25 words. Acknowledge the result
honestly and suggest one specific thing to work on. Write about "the student"
in the third person. Return only the sentence — no preamble, no quotation marks."""

    comment = ask(prompt)
    if comment is None:
        comment = "(comment unavailable)"

    results.append({
        "name": student["name"],
        "score": student["score"],
        "comment": comment,
        "subject": student["subject"],
    })




print(f"Generated {len(results)} comments.")

with open("comments.json", "w") as f:
    json.dump(results, f, indent=2)

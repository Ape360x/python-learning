import json
from groq_chat import ask
import sys

with open("data.json") as f:
    data = json.load(f)

results = []
failures = []

for student in data["students"]:
    prompt = f"""You are a teacher writing a short comment for a student's report card.

Score: {student["score"]} out of 100
Subject: {student["subject"]}

Write exactly one sentence, no more than 25 words. Acknowledge the result
honestly and suggest one specific thing to work on. Write about "the student"
in the third person. Return only the sentence — no preamble, no quotation marks."""

    try:
        comment = ask(prompt)
    except RuntimeError as e:
        print(f"Skipping {student['name']} - {e}")
        failures.append(student["name"])
        comment = "(comment unavailable)"

    results.append({
        "name": student["name"],
        "score": student["score"],
        "comment": comment,
        "subject": student["subject"],
    })




print(f"Wrote {len(results)} rows — {len(failures)} unavailable")
if failures:
    print(f"Failed: {', '.join(failures)}")

if len(failures) == len(results):
    print("Every request failed - comments.json left untouched.")
    sys.exit(1)
else:
    with open("comments.json", "w") as f:
        json.dump(results, f, indent=2)

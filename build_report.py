import html
import json

with open("data.json") as f:
    data = json.load(f)

with open("comments.json") as f:
    comments = json.load(f)

comments_by_name = {}
for row in comments:
    comments_by_name[row["name"]] = row["comment"]


def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


style = """
  body { font-family: system-ui, sans-serif; margin: 2rem; color: #111; }
  h1 { margin-bottom: 0; }
  .card { border: 1px solid #ddd; border-radius: 8px; padding: 1rem 1.25rem; margin-bottom: 1rem; }
  .grade { background: #111; color: #fff; border-radius: 999px; padding: 0.1rem 0.7rem; font-size: 0.8rem; vertical-align: middle; }
  .subject { color: #666; margin: 0.2rem 0; }
  .score { font-weight: bold; margin: 0.4rem 0; }
  .comment { margin: 0; }
  .legend { color: #666; font-size: 0.85rem; margin-top: 1.5rem; }
"""

cards = ""
for student in data["students"]:
    name = html.escape(student["name"])
    subject = html.escape(student["subject"])
    comment = html.escape(comments_by_name.get(student["name"], "(comment unavailable)"))

    cards += f"""
    <div class="card">
      <h2>{name} <span class="grade">{grade(student["score"])}</span></h2>
      <p class="subject">{subject}</p>
      <p class="score">{student["score"]} / 100</p>
      <p class="comment">{comment}</p>
    </div>"""

scores = [student["score"] for student in data["students"]]
average = sum(scores) / len(scores)

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>LockIn Gng — Student Report</title>
<style>{style}</style>
</head>
<body>
  <h1>LockIn Gng — Student Report</h1>
  <p>Overall average: {average:.2f} out of 100</p>
{cards}
  <p class="legend">Grades: 90+ A &middot; 80–89 B &middot; 70–79 C &middot; 60–69 D &middot; below 60 F</p>
</body>
</html>
"""

with open("report.html", "w", encoding="utf-8") as f:
    f.write(page)

print(f"Wrote report.html with {len(data['students'])} students.")
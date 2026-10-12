from groq_chat import ask

student = {"name": "Ada", "score": 78}

prompt = f"""You are a teacher writing a short comment for a student's report card.

Score: {student["score"]} out of 100

Write exactly one sentence, no more than 25 words. Acknowledge the result
honestly and suggest one specific thing to work on. Write about "the student"
in the third person. Return only the sentence — no preamble, no quotation marks."""


print(ask(prompt))
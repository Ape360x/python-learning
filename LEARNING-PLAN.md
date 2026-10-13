# Learning Plan — AI Automation & Coding

**Learner:** Tobi, 17 · **Started:** 2026-10-08
**Goal:** earn money online with AI automation + coding. Dropshipping is a *secondary* track, capped and unfunded until freelance income exists.

---

## Session rules

1. **Type everything. No copy-paste.** That's where the learning happens.
2. **When output is wrong, trace it by hand** — read the code top to bottom, write down what each variable holds after each pass. Don't guess at numbers.
3. **One concept at a time.** Build, run, show, then move on.
4. **Names must describe their contents.** If a name lies, change the name.

---

## Where we are — 2026-10-13 (session 5)

The learner can, unaided:
- write loops, conditionals and lists
- use built-ins: `sum()`, `max()`, `len()`
- use the **accumulator pattern** (tracker before loop, update inside, return after)
- define a **function** with `def`, a parameter, and `return`
- call a function with different data to prove reusability
- build and read **dictionaries** (key-value pairs, access, update, `in`, `.items()`)
- loop over a **list of dicts** — the shape every API returns
- read a **traceback** bottom-up and locate the fault from the error message
- read and write **files** — `open()`, `with`, `"r"`/`"w"`/`"a"`, `strip()`, `int()`
- separate reading and writing into different scripts instead of one that does both
- load **JSON** with `json.load()` and navigate nested dicts/lists
- split code across files with `import`, and guard module-level code with
  `if __name__ == "__main__":`

**Proved end to end:** `read_students.py` loads `data.json`, prints `success`,
`4`, `Bola`, `80.25` — using a `top_student` function written in a different file
two sessions earlier, on data it had never seen.

- make a real **API call** with `requests.get()` — GitHub's public API
- read `response.status_code`, and use `response.json()` to parse the body
- print `data.keys()` first when meeting a new API instead of guessing field names
- reuse a pattern across domains: `find_repo_with_most_stars` is `top_student`
  with four identifiers renamed

**Test technique learned:** the network is not needed to test logic. Feed the
function two or three fake dicts and run it — that caught the bug below in seconds.

- handle failure with `try` / `except` / `else` — catching **specific** exceptions,
  never a bare `except:`
- pass `timeout=` on every request, and use `raise_for_status()` to turn
  4xx/5xx responses into catchable exceptions
- test failure branches deliberately (fake username → 404, fake domain →
  ConnectionError, `timeout=0.001` → Timeout) instead of waiting for real breakage

- use **Git** — `init`, `status`, `add`, `commit`, `diff`, `remote`, `push`
- write a `.gitignore` **before** the first commit (1,006 `.venv` files kept out)
- understand local vs remote, and `origin` as the remote's nickname

**Live repository:** https://github.com/Ape360x/python-learning

- keep secrets out of code with **environment variables** — `.env` + `python-dotenv`,
  with `.env` in `.gitignore` and a committed `.env.example` as documentation
- make an **LLM API call** — `requests.post()`, `Authorization: Bearer` headers, a
  JSON body, and reading the reply from `data["choices"][0]["message"]["content"]`
- read and write **list comprehensions** — `[m["id"] for m in data]`
- wrap an API call in a reusable **`ask(prompt)`** function that returns the text
- design a **prompt** that behaves: `temperature` for consistency, third-person
  wording to stop the model using a name you never gave it, and `max_tokens=90`
  to stay under Groq's per-minute output-token limit
- loop a prompt over every student in `data.json` and collect the replies
- write **structured output** — `json.dump(results, f, indent=2)` to `comments.json`
- build a **lookup dict** from a list (`comments_by_name[row["name"]] = ...`) and
  merge two files **by key, never by position**
- return from a chain of `if`s — the first match wins, so the order of the tests matters
- generate **HTML** as a string with an f-string, and `html.escape()` every value
  that came from outside the program
- write text with `encoding="utf-8"`, and use a format spec like `{average:.2f}`

**Done end to end:** `write_comments.py` reads `data.json`, asks the model for one
report-card comment per student, and saves `comments.json` — JSON, list-of-dicts,
functions, an LLM API call, `try`/`except`, and rate-limit handling in one program,
committed and pushed as a portfolio piece.

**Done end to end:** `build_report.py` reads `data.json` (roster) and
`comments.json` (comments), merges them **by name** through a lookup dict, and
writes one self-contained `report.html` a parent can open and print. Overall
average 80.25, grades A–F, every inserted value passed through `html.escape()`.

**Next session starts at:** the open bug #22 — decide what a failed `ask()` should
return, and make its callers check, instead of silently getting `None`. Then Phase 2
continues with n8n / Make, the low-code tools most client work runs on.

---

## Bugs hit during the diagnostic (all fixed)

Worth re-reading — these are the classic beginner traps, already paid for:

1. `print()` indented inside the loop → printed 10 times instead of once
2. `count = 0` placed *inside* the loop → tally reset on every pass, answer came out 0
3. `i += 1` instead of `count += 1` → incremented the loop's own variable; Python overwrites it, so it does nothing
4. `count += 5` → a hardcoded constant. **A program must discover the answer from the data, never have it typed in.** Hardcoding breaks the moment the list changes.
5. A function named `count_evens` that returned `len(nums)` → right syntax, wrong job. A function that lies about what it does is worse than a badly named variable.
6. `def summarise(num)` that used the global `numbers` inside instead of `num` → the function secretly ignored its own input. It *looked* right because the list passed in happened to be the same as `numbers`. **A function may only use what it is passed.**
7. `print(summarise(...))` around a function with no `return` → printed `None`. `print` shows a value; `return` hands it back.
8. `(count)` on its own line → valid Python, does nothing. An expression with no `print` or `return` is discarded.
9. `students.items()` on a **list** → `AttributeError`. `.items()` is a dict method; lists have no keys.
10. `students[0]`, `students[1]`, `students[2]` hardcoded → same mistake as the `+= 5` constant. Survives only on a 3-item list.
11. `students()` → `TypeError: 'list' object is not callable`. Brackets mean "run this"; a list cannot be run.
12. `return` inside the loop → the function quits after the first item. Return goes **after** the loop.
13. Read *and* write in the same script → the append wasn't visible in the same run, and every run added another `100` permanently. **Non-reproducible:** the same code gave 82.3, then 84.5, then 86.2. Reading and writing belong in separate scripts.
14. `scores.txt` ended with no trailing newline, so appending `"100\n"` produced `55100` — two numbers merged into one. **Always end a file with a newline**, and guard reads with `if line:`.
15. `from students import top_students` ran `students.py` top to bottom, printing its test output first. Fixed with `if __name__ == "__main__":` — run directly it's `"__main__"`, imported it's the filename.
16. Dropped a return value again (`top_students(...)` with no `print`) → blank line where the answer should be. The tell is always a blank line or a stray `None`.
17. A side effect in an imported module: any module-level `print` or code fires on import, not just when you run the file.
18. **The ignored parameter, again.** `find_repo_with_most_stars(data)` looped over the global `repos` instead of `data`. Passing an empty list still returned a repo name — that was the proof. This is bug #6 recurring. **Checklist: after writing a function, confirm every declared parameter is actually used in the body.**
19. `if repo["stargazers_count"] > 100:` → a made-up threshold standing in for "the most". Same as bug #4. There is no number to invent; compare the items against each other.
20. Code after the `try`/`except` assumed the `try` had succeeded → `NameError: name 'repos' is not defined`. **Failure does not stop the file.** Any variable created inside `try` may not exist afterwards; success-path code belongs in `else:`.
21. **An API key was pasted into a chat.** It was revoked within minutes and never reached a file or the git history (verified with `grep` and `git log -S`). **Rule: a key that leaves your machine is burned — revoke first, ask questions later.** Revoking is free and instant, so never hesitate.
22. **Open item, not yet fixed:** `ask()` returns `None` when the request fails, because the `except` branch has no `return`. A caller doing `ask("...").upper()` would crash. Decide deliberately what a failed call should return — and make callers check.

---

## Curriculum

### Phase 1 — Python foundations (weeks 1–4)
- [x] Variables, lists, loops, conditionals
- [x] Built-in functions — `sum`, `max`, `len`
- [x] The accumulator pattern
- [x] First function (`def`, parameter, `return`)
- [x] Reading a traceback and locating the fault
- [x] Dictionaries — the data shape that APIs speak
- [x] Lists of dicts + the "best so far" tracker
- [ ] Functions deep — multiple parameters, default values, calling functions from functions
- [x] Reading and writing files — `with open()`, modes, line iteration
- [x] Side effects — read vs write, and why they must stay separate
- [x] Splitting code across files — `import`, and the `if __name__ == "__main__":` guard
- [x] Virtual environments — the project's private Python in `.venv`
- [x] `try` / `except` / `else` — specific exceptions, timeouts, testing failure branches
- [ ] Installing libraries with `pip` and virtual environments
- [x] Git and GitHub — `init`, `.gitignore`, `status`, `diff`, `add`, `commit`, `push`
- [x] Ignore rules — `.venv/`, `__pycache__/`, `.idea/`, `.DS_Store`, `*.pyc`
- [x] **Project:** a script that solves one real problem

### Phase 2 — APIs & automation (weeks 5–8)
- [x] JSON — reading and writing structured data (`json.load`, navigating nested dicts)
- [x] `json.loads` — the string version, via `response.json()` on API responses
- [x] HTTP requests — `requests.get()`, status codes, parsing the body
- [x] Calling an LLM API — Groq, `POST`, Bearer auth, reading the reply
- [x] Environment variables — `.env` + `python-dotenv`, and a committed `.env.example`
- [x] Revoking an exposed key, and verifying it never reached the repo
- [x] Prompt design — system messages, temperature, and writing prompts that work
- [x] **Project:** student-comment generator
- [x] **Project:** parent-facing `report.html` — merge two JSON files by name, build escaped HTML, write utf-8
- [ ] n8n or Make — the low-code automation tools most client work uses
- [ ] Webhooks — letting other apps trigger your code
- [ ] **Project:** 3 portfolio automations, each with a written one-pager

### Phase 3 — Getting paid (weeks 9–12)
- [ ] Pick one niche and stay in it
- [ ] Rebuild the Flask portfolio to sell a service, not to list skills
- [ ] Write an outreach message; 10 per day
- [ ] Free audits → paid builds
- [ ] Pricing: simple automation, bigger build
- [ ] **Goal: 1–3 paying clients**

### Dropshipping track — capped at 2 hours/week
- [ ] Validate demand organically (TikTok / Reddit / Facebook groups). No ad spend.
- [ ] No Shopify subscription until Phase 2 income exists
- [ ] Better angle: sell automation *to* dropshippers and ecommerce stores instead of competing with them

---

## Getting paid from Nigeria

- International clients pay many times local rates — aim the portfolio outward
- Payment: Paystack, Flutterwave, or a USD account service (Grey, Geegpay)
- At 17 most payment processors want 18+ — a parent will likely need to be involved. Sort this before the first client, not after.

---

## Existing work worth revisiting

- `PycharmProjects/PythonProject` — early Python exercises
- `Documents/.../portfolio-flask-3/app.py` — Flask app with SQLAlchemy. Has `SECRET_KEY = "dev-secret-change-this"` hardcoded; move it to an environment variable before it ever goes public.
- `Desktop/last-period-pygame` — 770 lines across 6 files
- `Desktop/last-period-roblox`

---

## Health / off-screen

Training plan and workout tracker live in `~/outputs/01a11a2f-0e7d-7ad3-9574-1c3e7b6973e5/`.

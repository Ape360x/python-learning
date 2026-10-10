scores = []
with open("scores.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            scores.append(int(line.strip()))

print(scores)
print(len(scores))
print(sum(scores))
print(sum(scores) / len(scores))
print(max(scores))
import sys

question = sys.stdin.readline().rstrip()
question = question.replace(". ", "/ ").split("/ ")
new = list()
for q in question:
    print(q)
    if "?" in q:
        save = q.replace("? ", "/").replace("?", "").split("/")
        for s in save:
            new.append(s)

res = list()
for q in new:
    if "What is" in q:
        res.append("Forty-two is" + q[7:] + ".")

for r in res:
    print(r)

import sys

input = sys.stdin.readline

n = input().rstrip()

pn = [0 for _ in range(10)]

for i in range(len(n)):
  cnt = int(n[i])
  if cnt == 6 or cnt == 9:
    if pn[6] <= pn[9]:
      pn[6] += 1
    else:
      pn[9] += 1
  else:
    pn[cnt] += 1
    
print(max(pn))

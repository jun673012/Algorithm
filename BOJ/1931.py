n = int(input())

t = []

for _ in range(n):
  s, f = map(int, input().split())
  t.append([s, f])

t = sorted(t, key=lambda x: x[0])
t = sorted(t, key=lambda x: x[1])

e = 0
cnt = 0

for i, j in t:
  if i >= e:
    cnt += 1
    e = j

print(cnt)

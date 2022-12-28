a = int(input())
N = []
for i in range(a):
  N.append(int(input()))
N.reverse()
tmp = 0
cnt = 0
for i in range(a):
  if N[i] > tmp:
    tmp = N[i]
    cnt += 1

print(cnt)

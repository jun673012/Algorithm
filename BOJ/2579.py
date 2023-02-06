n = int(input())

d1 = [0] * 301
d2 = [0] * 301

for i in range(n):
  d1[i] = int(input())

d2[0] = d1[0]
d2[1] = d1[0] + d1[1]
d2[2] = max(d1[1] + d1[2], d1[0] + d1[2])

for i in range(3, n):
  d2[i] = max(d2[i - 3] + d1[i - 1] + d1[i], d2[i - 2] + d1[i])
  
print(d2[n - 1])

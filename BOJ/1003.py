t = int(input())

z = [1, 0, 1]
o = [0, 1, 1]

for _ in range(t):
  n = int(input())
  if len(z) <= n:
    for i in range(len(z), n + 1):
      z.append(z[i - 1] + z[i - 2])
      o.append(o[i - 1] + o[i - 2])
  print(z[n], o[n])

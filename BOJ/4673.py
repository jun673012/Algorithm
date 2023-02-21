n = [i for i in range(1, 10001)]

for i in range(1, 10001):
  res = i 
  tmp = i
  for _ in range(len(str(i))):
    res += tmp % 10
    tmp = tmp // 10
  if res in n:
    n.remove(res)
    
for i in n:
  print(i, end='\n')

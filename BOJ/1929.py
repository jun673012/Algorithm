import sys
import math

input = sys.stdin.readline

m, n = map(int, input().split())

array = [True for i in range(n + 1)] 

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: 
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1
          
if m < 2:
  m = 2
  
for i in range(m, n + 1):
    if array[i]:
        print(i, end='\n')

import sys

input = sys.stdin.readline

n = int(input())
maxCom = 0

for i in range(n):
  plug = int(input())
  maxCom += plug - 1
  
print(maxCom + 1)

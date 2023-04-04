import sys

input = sys.stdin.readline

n = input()

hnt = n.count(':-)')
snt = n.count(':-(')

if hnt == 0 and snt == 0:    
  print('none')
elif hnt > snt:
  print('happy')
elif hnt < snt:
  print('sad')
elif hnt == snt:
  print('unsure')

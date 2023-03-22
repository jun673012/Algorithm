import sys

input = sys.stdin.readline

pnt = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
grd = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
s = 0
res = 0
for i in range(20):
  a, b, c = input().split()
  b = float(b)
  if c != "P":
    s += b
    res += b*grd[pnt.index(c)]
  
print(format(res/ s, ".6f"))  

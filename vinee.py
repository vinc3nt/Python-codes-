n = input()
n= int(n)
s = input().split()
d = input().split()
for i in range(n):
  int(d[i])= int(d[i])//int(s[i])
for i in  range(n):
  if d[i] < temp:
    temp = d[i]
print(temp)
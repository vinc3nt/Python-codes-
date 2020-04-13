n = input()
n= int(n)
s = input().split()
d = input().split()
temp= int(d[0])//int(s[0])
for i in range(n):
    d[i]= int(d[i])//int(s[i])
for i in  range(n):
  if int(d[i]) < temp:
    temp = d[i]
print(temp)
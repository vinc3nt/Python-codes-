m = input()
m = int(m)
for z in range(m):
    n = int(input())
    s = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]
    s.sort(reverse = True)
    d.sort()
    i = 0
    count =0
    temp = int()
    while(i<n):
        x=0
        temp = -1
        for x in range(n-i):
            if(s[0]<=d[x]):
                break
            elif s[0] >d[x]:
                temp = x
        if temp == -1:
            break
        count= count+1
        del s[0]
        del d[temp]
        i =i+1
    print(count)
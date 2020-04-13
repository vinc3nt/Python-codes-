m = input()
m = int(m)
while(m):
    n = int(input())
    s = input()
    d = input()
    s = list(map(int, s.split()))
    d = list(map(int, d.split()))
    s.sort(reverse = True)
    d.sort()
    i = 0
    count =0
    temp = int()
    while(i<n):
        x=0
        temp = -1
        while(x <n-i ):
            if(s[0]<=d[x]):
                break
            elif s[0] >d[x]:
                temp = x
            x = x+1
        if temp == -1:
            break
        count= count+1
        del s[0]
        del d[temp]
        i =i+1
    print(count)
    m = m-1
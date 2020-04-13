
m = input()
m = int(m)
for z in range(m):
    n = input() #
    n= int(n)
    s = input()#
    s= s.split()
    d = input()#
    d= d.split()
    for i in range(n):
        s[i]= int(s[i])
        d[i]= int(d[i])
    #print(s)
    #print(d)
    s.sort(reverse = True)
    d.sort()
    i = 0
    count =0
    #print(s)
    #print(d)
    temp = int()
    while(i<n):
        x=0
        temp = -1
        for x in range(n-i):
            if(s[0]<d[x]):
               # if(temp != -1):
                #    count= count + 1
                break
            elif s[0] >d[x]:
                temp =x
        if temp == -1:
            break
        #print(s[0], d[temp])
        count= count+1
        del s[0]
        del d[temp]
        i =i+1
    print(count)
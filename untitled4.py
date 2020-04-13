n = int(input())
for i in range(n):
    l= int(input())
    lis= input()
    lis= lis.split()
    m =True
    lo =int()
    lo = l-1
    while(lo >= 0 and m ==True):
        maxe= (int(lis[lo-n+1]) + int(lis[lo]))
        maxa= (int(lis[lo-n+1+1]) + int(lis[lo-1])
        if maxe == maxa:
            m= False
    if(m== True):
        print("Yes")
    else:
        print("No")

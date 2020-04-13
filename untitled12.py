import numpy
t=int(input())
for i in range(t):    
    n=int(input())    
    tg=list(map(int,input().split())) 
    tg = numpy.asarray(tg)
    op=list(map(int,input().split()))  
    op = numpy.asarray(op)
    cnt=0    
    op[::-1].sort()
    tg[::-1].sort()
    print(op)
    for i in range(n):        
        for j in range(len(op)):            
            if tg[i]>op[j]:                
                cnt+=1       
                op = numpy.delete(op,j)
                break   
    print(cnt)
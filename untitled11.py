t=int(input())
for i in range(t):    
    n=int(input())    
    tg=list(map(int,input().split()))    
    op=list(map(int,input().split()))    
    cnt=0    
    tg.sort(reverse=True)    
    op.sort(reverse=True)    
    for i in range(n):        
        for j in range(len(op)):            
            if tg[i]>op[j]:                
                cnt+=1                
                op.pop(j)                
                break    
    print(cnt)


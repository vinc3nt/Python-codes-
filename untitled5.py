## import the important module in python 
import numpy as np 
              
# make matrix with numpy 

na = input()
na = int(na)

for x in range(na):
    rowlen= 0
    collen=0
    n = input()
    n= int(n)
    d= "["
    for i in range(n):
        s= input()
        d= d+ s.replace(" ", ",")
        d= d+";"
        d= d+" "
        s=set((s.replace(",","")).split())
        if (n-len(s)) > 0 :
            rowlen= rowlen+ 1
    
    #print(d)
    d= d[:-2]
    d= d+"]"
    #print(d)
    #print(d)
    gfg = np.matrix(d) 
    #print(gfg)
                  
    # applying matrix.trace() method 
    geek = gfg.trace() 
    
    geek=int(geek)
    gfg = gfg.transpose()
    #print(gfg)
    for z in range(n):
        m= str(gfg[z])
        m=m.replace("[","")
        m=m.replace("]","")
        m=m.replace(" ","")
        m=set(m)
        #print(m)
        m= n-len(m)
        if m > 0:
            collen= collen+ 1
    #collen = len(collen)
    print("Case #"+ str(x+1) + ":" +" "+ str(geek)+ " " +str(rowlen) + " " +str(collen))
           #1: 4 0 0

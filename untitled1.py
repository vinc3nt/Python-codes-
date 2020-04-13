# import the important module in python 
import numpy as np 
              
# make matrix with numpy 

na = input()
na = int(na)
for x in range(na):
    n = input()
    n= int(n)
    d= "["
    for i in range(n):
        s= input()
        d= d+ s.replace(" ", ",")
        d= d+";"
        d= d+" "
    
    #print(d)
    d= d[:-2]
    d= d+"]"
    #print(d)
    gfg = np.matrix(d) 
                  
    # applying matrix.trace() method 
    geek = gfg.trace() 
        
        #print(geek) 
    #geek=int(geek)
    unq, count = np.unique(gfg, axis=0, return_counts=True)
    repeated_groups = unq[count > 1]
    rowlen= len(repeated_groups)
    
    gfg = gfg.transpose()
    #print(count)
    unq, count = np.unique(gfg, axis=0, return_counts=True)
    repeated_groups = unq[count > 1]
    collen= len(repeated_groups)
    geek=int(geek)
    #collen = len(collen)
    print("Case #"+ str(x+1) + ":" + str(geek)+ " " +str(rowlen) + " " +str(collen))

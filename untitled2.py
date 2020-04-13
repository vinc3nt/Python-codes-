n = int(input())
dic =dict()
while(n > 0 ):
    x= input()
    print("loop n")
    s=0
    s= x.split()
    dic1={s[0] : [ s[1],s[2],s[3] ]}
    dic.update(dic1)
    #print(dic["vin"])
    
    n= n-1
    

print(sum/3)
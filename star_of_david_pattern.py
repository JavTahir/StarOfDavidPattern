
def count(x):
    # Calculate the center as (x + 1) // 2
    return (x + 1) // 2


    

            



 

def lowertriangle(x,type):

    row = 0
    if(type==0):
        row = 5

    elif(type==1):
        row = 7


    for i in range(row,0,-2):
        n = x-i
        y = int(n/2)
        for j in range (0,y):
            print(" ",end="  ")
        for star in range(0,i):
            print("*",end="  ")
        
        for j in range (0,y):
            print(" ",end="  ")
        print("\n")




def lowershape(x,limit,type):
    n = x
    for i in range (limit,0,-1):
        n = n + 2
        for v in range(1,i):
            print(" ",end="  ")
        for j in range(0,n):
            print("*",end="  ")
        for v in range(1,i):
            print(" ",end="  ")
        print("\n")
    lowertriangle(n,type)
        


def uppershape(x,limit,type):
    n = x
    for i in range(0,limit):
        for v in range(1,i+1):
            print(" ",end="  ")
        for j in range(0,n):
            print("*",end="  ")
        for v in range(1,i+1):
            print(" ",end="  ")
        n = n-2
        print("\n")
    lowershape(n+2 ,limit-1,type)



def uppertriangle(x,limit,type):

    row = 0
    if(type==0):
        row = 3

    elif(type==1):
        row = 4
    
    n = x
    for i in range(0,row):
        n = n-1
        y = n/2
        for j in range (0,n):
            if(j==y):
                for star in range(i,3*i+1):
                    print("*",end="  ")
            print(" ",end="  ")
        n = n-1
        print("\n")
    
    upper = int(limit/2)+1
    uppershape(x,upper,type)


        
        
        

    

x = int(input("Enter star number:"))


center =  count(x) 
type = 0
mid = 0
print(center)
if(center % 2 == 0):
    type=0
    mid = int(center-3)

elif(center % 2 != 0):
    type=1
    mid = int(center-4)


    
print(type)   


print(mid)
uppertriangle(int(x),mid,type)








             


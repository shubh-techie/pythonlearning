
# print(8%2==0)
# print(9%2==0)
# print(10%2==0)

a=8
if a%2==0:
    print("8 is an even number")

# a = 8
# if a % 2 == 0: # If the number is divisible by 2
#     print(a,"is a odd number")
# else:
#     print(a,"is an even number")

#....


value = 5
if value>0:
    print("The value is positive")
else:
    print("The value is negative")


#---------------------------

x = int(input("enter value x:"))
y = int(input("enter value of y:"))

if(x>0 and y>0):    
  print("x and y are positive")
else:
    if(x<0 and y >= 0):    
     print("x or y is second quarant")
    else:
        if(x<0 and y < 0):    
           print("x or y is third quarant")
        else:
            if(x>0 and y < 0):    
               print("x or y is fourth quarant")
            else:
                print("x and y are zero")

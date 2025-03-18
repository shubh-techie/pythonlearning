age  = int(input("Enter your age:"))
if age>= 18:
    print("You are an adult")
else:
    print("You are a minor")

# sum of the digit 

sum = 0
number = int(input("Enter a number with almost 4 digits :"))

if (number >0 and number < 10000):
    sum = sum + number %10
    number = number //10 
    if(number>0):
        sum = sum + number %10
        number = number //10
    if(number>0):
        sum = sum + number %10
        number = number //10
    if(number>0):
        sum = sum + number %10
        number = number //10
    print("The sum of the digits is: ", sum)       
else:
    print("Not a valid number")  



number = int(input("Enter a number :"))
if (number > 10 and number < 99):
    print("The number is a two digit number")
else:
    print("The number is not a two digit number")




a = int(input("Enter the number:")) # Taking input in variable a
while a > 0: # This loop will terminate when the value of a is not greater than 0
  print(a % 10 )
  a //=10 # Dividing a by 10 and assigning the result to variable a
print()

a = 1
sum = 0
while a!=0:
    a = int(input("Enter the number:")) 
    sum += a
print("sum is : ", sum)

a = 1
while a < 1000:
    print(a)
    a *= 3

a = 1
totalSum = 0
count = 0
while a != 0:
    count += 14
    x = int(input("Enter the number:"))
    totalSum +=x;
print("Average is: ", totalSum/count)

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

result = 3 * x + 5 * y
print("The calculated result is: ", result)

for a in [0,1,2,3]:
     print(a , end="")

for a in [1,2,3,4]:
    e = a*2
    print(e)

for a in [1,3,5,7,9]:
    print(a)

arr = [1,2,3,4,5]
for a in arr:
    print(a*2 -1)

for a in range(1, 101):
    print(a, end=" ")

for a in range(1,11):
    print(a * 15, end=" ")

print("")
print("      *")
print("     * *")
print("    * * *")
print("   * * * *")
print("  * * * * *")
print(" * * * * * *")


for a in range(0,200,20):
    print(a, end=" ")

for a in range(1,201,2):
    print (a)

for a in range(1,101,5):
    print(a, end=" ")

num = int(input("enter the number: "))
for a in range(1,10):
   print(num, "x", a, "=", num*a)

for a in range(1, 100, 2):
    print(a)

x = int(input("How many number:"))
sum =0
for a in range(x):
    print("a:", a)
    num = int(input("Enter the number:"))
    sum += num

if(sum > 0):
    print("mean :", sum//x)


x = int(input("Enter the number: "))

for a in range(1, x+1):
    if x % a ==0:
        print(a, end=" ")
    
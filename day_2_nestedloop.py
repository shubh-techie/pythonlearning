# for a in ['a','b','c','d']:
#     for m in [1,2,3,4]:
#         print(a, m, end="\t")

# for a in range(1,5):
#     for m in range (1,5):
#         print("( ", a, m, ")", end="\t")
#     print()

loopNumber = int(input("Enter the number of loop: "))

for a in range(loopNumber):
    for m in range (loopNumber):
        print("*", end="")
    print()

x = int(input("enter first number"))
y = int(input("enter second number"))

for a in range(x):
    for m in range (y):
        print("*", end="")
    print()


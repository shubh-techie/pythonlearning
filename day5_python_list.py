


def arerage(arr):
    return sum(arr)/len(arr)

def Average(arr):
    sum =0
    for i in arr:
        sum+=i
    n = len(arr)
    return sum/n

arr = [10, 20, 30, 40, 50]
average = Average(arr)
print(average) # 30.0



def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sorted_arr = BubbleSort(arr)
print(bubble_sorted_arr) # [11, 12, 22, 25, 34, 64, 90]









arr = [10,20,20,20,30,40,50]

print(arr[0]) # 10
print(arr[1]) # 20
print(arr[2]) # 30
print(arr[3]) # 40
print(arr[4]) # 50  

print(arr[-1]) # 50
print(arr[-2]) # 40
print(arr[-3]) # 30
print(arr[-4]) # 20 
print(arr[-5]) # 20 

arr.remove(20)
print(arr) # [10, 20, 30, 40, 50]
print(arr.pop())
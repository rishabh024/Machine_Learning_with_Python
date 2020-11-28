# Developed By : Rishabh Gupta

# Question is-  : Write a Python program for binary search.


def binarySearch(array, x, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = list(map(int, input("enter soace separated nos. for an array--").split()))
x = eval(input("enter the no for searching--"))
arr_sorted = sorted(array)

result = binarySearch(arr_sorted, x, 0, len(array)-1)

# to give the index of a no found in the original array, after the binary search operation
if result != -1:
    for i in range(len(array)):
        if x == array[i]:
            print("Element is present at index ", i )
else:
    print("Not found")

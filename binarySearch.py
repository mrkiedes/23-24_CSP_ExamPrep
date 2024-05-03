# Binary Search in python


def binarySearch(array, x, low, high):
     if high >= low:
         mid = low + (high - low) // 2
         #If value is at mid, return it
         if array[mid] == x:
             return mid
         # Search the left half
         elif array[mid] > x:
             return binarySearch(array, x, low, mid - 1)
         # If not in the left, search the right
         else:
            return binarySearch(array, x, mid + 1, high)
     else:
        return -2





array = [3, 4, 5, 6, 7, 8, 9]
x = 42

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
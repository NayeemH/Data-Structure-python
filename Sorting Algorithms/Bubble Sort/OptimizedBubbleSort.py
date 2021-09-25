
# Python program for implementation of Bubble Sort
#Author-Nayeem Hasan


def BubbleSort(array):
    arraySize = len(array)

    # Traverse through all array elements
    for i in range(arraySize):
        swapped = False

        # Last i elements are already in place

        for j in range(0, arraySize-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break

# Driver code to test above
array = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(array)

print ("Sorted array is:")
print(array)
def mergeSort(arr):
    if len(arr)>1:
         # Finding the mid of the array
        mid = len(arr)//2

         # Dividing the array elements
        left_array = arr[:mid]
        right_array = arr[mid:]

        # Sorting the first half
        mergeSort(left_array)

        # Sorting the second half
        mergeSort(right_array)


        i = 0 #for left array
        j = 0 # for right array
        k = 0 # merge array index

        # Copy data to temp arrays Left_array[] and Right_array[]
        while i<len(left_array) and j<len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1
        
        # Checking if any element was left

        while i< len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1
        while j< len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1
            






arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
print(arr)
mergeSort(arr)
print("Sorted array is: ", end="\n")
print(arr)


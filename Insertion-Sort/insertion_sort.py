def InsertionSort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j = j -1
        array[j+1] = key


arr = [12, 11, 13, 5, 6]
InsertionSort(arr)
print(arr)
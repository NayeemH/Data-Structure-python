# Max Heap Needed

from Heap.heap import buildMaxHeap


def heapSort(array):
    n = len(array)


    for i  in range(n//2-1, -1, -1):
        buildMaxHeap(array)

    for i in range(n-1,0,-1):
        array[i],array[0] = array[0], array[i]
        buildMaxHeap(array)

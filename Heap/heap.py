def MaxHeap(A,k):
    l = left(k)
    r = right(k)
    if l<len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k

    if r< len(A) and A[r] > A[largest]:
        largest = r
    
    if largest !=k:
        A[k], A[largest] = A[largest], A[k]


def left(k):
    return 2*k +1
    
def right(k):
    return 2*k + 2

def buildMaxHeap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1,-1):
        MaxHeap(A,k)


A = [3,9,2,1,4,5]
buildMaxHeap(A)
print (A)

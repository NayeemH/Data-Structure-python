#Selection sort -python
#Author-Nayeem Hasan

A = [32,54,12,34,11,9,7,56,43,25]

# Travers through the array elements
for i in range(len(A)):
    # find the minimun element from the array
    min_idx = i

    for j in range(i+1,len(A)):
        if A[min_idx] > A[j]:
           min_idx = j 

    # swap the minimum item with the first item
    A[i],A[min_idx] = A[min_idx], A[i]

# driver code to test
print( "Sorted array")
print(A)
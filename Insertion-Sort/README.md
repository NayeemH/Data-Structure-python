# Insertion Sort
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Algorithm 
To sort an array of size n in ascending order: 
1. Iterate from arr[1] to arr[n] over the array. 
2. Compare the current element (key) to its predecessor. 
3. If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
## Example: 
* 12, 11, 13, 5, 6
* Let us loop for i = 1 (second element of the array) to 4 (last element of the array)
* i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12 
* 11, 12, 13, 5, 6
* i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13 
* 11, 12, 13, 5, 6
* i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position. 
* 5, 11, 12, 13, 6
* i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position. 
* 5, 6, 11, 12, 13 

### Time Complexity: O(n^2) 
### Auxiliary Space: O(1)
### Boundary Cases: 
Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
### Algorithmic Paradigm: Incremental Approach
### Sorting In Place: Yes
### Stable: Yes
### Online: Yes
### Uses: 
Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.



# Recursive Insertion Sort
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
Below is an iterative algorithm for insertion sort
### Algorithm 
// Sort an arr[] of size n
insertionSort(arr, n) 
    Loop from i = 1 to n-1.
       a) Pick element arr[i] and insert
          it into sorted sequence arr[0..i-1] 

## How to implement it recursively? 
Recursive Insertion Sort has no performance/implementation advantages, but can be a good question to check one’s understanding of Insertion Sort and recursion.
If we take a closer look at Insertion Sort algorithm, we keep processed elements sorted and insert new elements one by one in the inserted array.
## Recursion Idea. 

1. Base Case: If array size is 1 or smaller, return.
2. Recursively sort first n-1 elements.
3. Insert last element at its correct position in sorted array.

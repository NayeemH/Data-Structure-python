def Partition(start_idx,end_idx, array):
	pivot_idx = start_idx
	pivot = array[start_idx]

	while start_idx<end_idx:
		while start_idx<len(array) and array[start_idx]<=pivot:
			start_idx= start_idx +1

		while array[end_idx] > pivot:
			end_idx = end_idx -1

		if( start_idx < end_idx):
			array[start_idx], array[end_idx] = array[end_idx], array[start_idx]

	array[end_idx],array[pivot_idx] = array[pivot_idx], array[end_idx]

	return end_idx


def quickSort(start_idx,end_idx, array):
	if(start_idx<end_idx):

		x = Partition(start_idx,end_idx, array)

		quickSort(start_idx, x-1, array)
		quickSort(x+1, end_idx, array)

	
array = [5,6,2,7,1,9,11]
quickSort(0,len(array)-1,array)
print(array)

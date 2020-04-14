def quick_sort(A, low=None, hi=None):
    if low is None or hi is None:
        quick_sort(A, 0, len(A)-1)
    elif low < hi:
	    p = partition(A, low, hi)
	    quick_sort(A, low, p - 1)
	    quick_sort(A, p + 1, hi)
	
def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])

	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid

	return hi
	
def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return (border)


if __name__ == '__main__':
    numbers_list = [17, 41, 5, 22, 54, 6, 29, 3, 13]

    print(numbers_list)
    quick_sort(numbers_list)
    print(numbers_list)
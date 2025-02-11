def min_heapify(A, k):
	l = 2 * k + 1
	r = 2 * k + 2
	if l < len(A) and A[l] < A[k]:
		s = l
	else:
		s = k
	if r < len(A) and A[r] < A[s]:
		s = r
	if s != k:
		A[k], A[s] = A[s], A[k]
		min_heapify(A, s)


def build_min_heap(A):
	n = int((len(A) // 2) - 1)
	for k in range(n, -1, -1):
		min_heapify(A, k)

from typing import Any, Sequence, Optional
from random import randint


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	arr.sort()
	print(elem, arr)

	mid = len(arr) // 2
	low = 0
	high = len(arr) - 1

	flag = 0

	while arr[mid] != elem and low <= high:
		if elem > arr[mid]:
			low = mid + 1
		else:
			high = mid - 1
		mid = (low + high) // 2

		#if elem <

	for i in arr:
		print(i)
		if i != elem:
			return None
		else:
			return mid


	return mid


def test ():

	# Создание списка,
	# его сортировка по возрастанию
	# и вывод на экран
	a = []
	for i in range(15):
		a.append(randint(1, 50))
	a.sort()
	print(a)

	# искомое число
	value = int(input())

	mid = len(a) // 2
	low = 0
	high = len(a) - 1

	while a[mid] != value and low <= high:
		if value > a[mid]:
			low = mid + 1
		else:
			high = mid - 1
		mid = (low + high) // 2

	if low > high:
		print("No value")
	else:
		print("ID =", mid)
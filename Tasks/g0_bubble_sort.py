from typing import Collection, TypeVar
import random


_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	container
	for i in range(len(container)-1):
		for j in range(len(container) - 1):
			if container[j] > container [j+1]:
				container[j], container[j+1] = container[j+1], container[j]


	return container

def with_for_example():
	N = 10
	a = []
	for i in range(N):
		a.append(random.randint(1, 99))
	print(a)

	for i in range(N - 1):
		for j in range(N - i - 1):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]

	print(a)

def with_wile_example():
	N = 10
	a = []
	for i in range(N):
		a.append(random.randint(1, 99))
	print(a)

	i = 0
	while i < N - 1:
		j = 0
		while j < N - 1 - i:
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
			j += 1
		i += 1

	print(a)

def bubble(array):
	for i in range(n-1):
		for j in range(n-i-1):
			if array[j] > array[j+1]:
				buff = array[j]
				array[j] = array[j+1]
				array[j+1] = buff

def with_py_function_example():
	#N = 10
	a = []
	for i in range(n):
		a.append(random.randint(1, 99))

	print(a)
	bubble(a)
	print(a)


if __name__ == "__main__":

	n = 10
	#shuffle_list = list(range(n))
	shuffle_list = [1, 0, 4, 2, 3]
	random.shuffle(shuffle_list)
	print(shuffle_list)
	print(sort(shuffle_list))
	print()

	with_for_example()
	print()
	with_wile_example()
	print()
	with_py_function_example()
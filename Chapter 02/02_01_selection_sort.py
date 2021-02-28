#!/usr/bin/python

# Функция возвращает индекс минимального элемента

def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index
	

# функция сортировки выбором

def selectionSort(arr):
	sorted_arr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		sorted_arr.append(arr.pop(smallest))
	return sorted_arr
	

print(selectionSort([5, 3, 6, 2, 10]))

# Jakub Dębski, 405600
from typing import List

def quicksort(input_lst: List[int]) -> List[int]:
    def quicksort_inplace(lst: List[int], start: int, stop: int) -> List[int]:
        i = start
        j = stop
        pivot = (i + j) // 2
        while i < j:
            while lst[i] < lst[pivot]:
                i += 1
            while lst[j] > lst[pivot]:
                j -= 1
            if i <= j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        if start < j:
            quicksort_inplace(lst, start, j)
        if i < stop:
            quicksort_inplace(lst, i, stop)

        return lst

    copy_of_input_lst = input_lst.copy()
    quicksort_inplace(copy_of_input_lst, 0, len(copy_of_input_lst)-1)

    return copy_of_input_lst


def bubblesort(input_lst: List[int]) -> (List[int], int):
    copied_lst = input_lst.copy()
    n = len(copied_lst)
    counter = 0
    while n > 1:
        flag = True
        for i in range(1, n):
            if copied_lst[i-1] > copied_lst[i]:
                copied_lst[i-1], copied_lst[i] = copied_lst[i], copied_lst[i-1]
                flag = False
            counter += 1
        n -= 1
        if flag:
            break
    return copied_lst, counter


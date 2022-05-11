"""iterative quicksort algorithm module"""


def partition(array, start, end):
    """Split`s list by pivot. [Lt pivot) & [Gt pivot]
    :arg array -- ur array
    :arg start -- 0pos
    :arg end -- -1pos
    :return pivot_i -- pivot index"""
    pivot = array[end]
    pivot_i = start

    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[pivot_i] = array[pivot_i], array[i]
            pivot_i += 1
    array[end], array[pivot_i] = array[pivot_i], array[end]
    return pivot_i


def quick_sort(u_array):
    """Iterative quicksort method
    :arg u_array -- unsorted list
    """
    stack = list()
    start = 0
    end = len(u_array) - 1
    stack.append((start, end))

    while stack:
        pivot = partition(u_array, start, end)
        start, end = stack.pop()
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
        if pivot + 1 < end:
            stack.append((pivot + 1, end))


if __name__ == '__main__':
    arr = [5, 9, 8, 6, 3, 2, 4, 1, 7]
    arr2 = [56, 92, 84, 16, 36, 23, 74, 31, 67]
    print(arr, "\n\n")
    quick_sort(arr)
    print(arr, "\n\n")
    print(arr2, "\n\n")
    quick_sort(arr2)
    print(arr2, "\n\n")



def binary_search(array, element):
    """Binary search method"""
    start = 0
    end = len(array)
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == element:
            return mid
        if array[mid] > element:
            end = mid - 1
        else:
            start = mid

    return "No such element!"


if __name__ == '__main__':
    looking_for = 16
    list_to_search = [1, 2, 5, 7, 13, 15, 16, 19, 24, 27, 32]

    print(f"Searching for {looking_for}")
    print(f"Index of {looking_for}: {binary_search(list_to_search, looking_for)}")


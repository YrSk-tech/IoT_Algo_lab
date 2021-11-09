def find_triplet(array, sum):
    """
    :param array: array of numbers to find a triplet
    :param sum: a sum for 3 numbers
    :return: returning a triplet of numbers
    >>> find_triplet([1,3,4,4,5],12)
    3 , 4 , 5
    >>> find_triplet([5,3,2,6,7,5],1)
    Sorry, there is no triplet
    >>> find_triplet([10,23,43,67,54],144)
    23 , 54 , 67
    >>> find_triplet([2,2,2], 6)
    2 , 2 , 2
    >>> find_triplet([2,2,9], 6)
    Sorry, there is no triplet
    """
    length = len(array)
    if length >= 1000 or length < 3 or sum >= 3 * pow(10, 9):
        return
    quicksort_asc(array, 0, length - 1)
    for i in range(0, length - 2):
        first_element = i + 1
        last_element = length - 1
        while first_element < last_element:
            if array[i] + array[first_element] + array[last_element] == sum:
                return print(array[i], ',', array[first_element], ',', array[last_element])
            elif array[i] + array[first_element] + array[last_element] < sum:
                first_element += 1
            else:
                last_element -= 1
    return print('Sorry, Ilona, there is no triplet for this num =(')


def quicksort_asc(array, bottom_index, top_index):
    """
    :param array: array of numbers to sort
    :param bottom_index: first element of array
    :param top_index: last element of array
    :return: returning sorted array
    >>> quicksort_asc([4,3,6], 0, 2)
    [3, 4, 6]
    """
    if len(array) == 1:
        return
    if bottom_index < top_index:
        pivot_index = partition(array, bottom_index, top_index)
        quicksort_asc(array, bottom_index, pivot_index - 1)
        quicksort_asc(array, pivot_index + 1, top_index)
    return array


def partition(array, bottom_index, top_index):
    pivot = array[top_index]
    smaller_element = bottom_index - 1
    for iterator in range(bottom_index, top_index):
        if array[iterator] <= pivot:
            smaller_element += 1
            array[smaller_element], array[iterator] = array[iterator], array[smaller_element]
    array[smaller_element + 1], array[top_index] = array[top_index], array[smaller_element + 1]
    return smaller_element + 1


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
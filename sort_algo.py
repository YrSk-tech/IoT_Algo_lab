from Counters import Counter


def mergeSort(array, sort_method):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        mergeSort(left_half, sort_method)
        mergeSort(right_half, sort_method)

        i = 0
        j = 0
        k = 0


        while i < len(left_half) and j < len(right_half):
            Counter.merge_compare_count += 1
            if sort_method == 1:
                sorting_by_method = left_half[i] >= right_half[j]
            else:
                sorting_by_method = left_half[i] <= right_half[j]
            if sorting_by_method:
                array[k] = left_half[i]
                i += 1
                Counter.merge_swap_count += 1
                Counter.merge_compare_count += 1
            else:
                array[k] = right_half[j]
                j += 1
                Counter.merge_swap_count += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
            Counter.merge_swap_count += 1
            Counter.merge_compare_count += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
            Counter.merge_swap_count += 1
            Counter.merge_compare_count += 1




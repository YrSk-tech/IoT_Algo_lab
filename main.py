import datetime
import time

from Counters import Counter
from sort_algo import mergeSort

if __name__ == '__main__':
    input_data = [2, 1, 5, 4, 32, -2, -5, 54, 4, 657, 34, 76, 9, 234, 54, 98, 66, 666, -2, 456, 96, -2222]
    sort_method = bool()
    print("Data to sort:", input_data)
    sort_method = int(input("Ascending - 0 , Descending - 1:"))
    sort_time_begin = time.time()
    mergeSort(input_data, sort_method)
    sort_time_end = time.time() - sort_time_begin
    sort_time = (sort_time_end - sort_time_begin) * 1000
    print("Sorted data by")
    if sort_method == 1:
        print("Descending:", input_data)
    else:
        print("Ascending:", input_data)
    print("\nAmount of swaps: ", Counter.merge_swap_count,
          "\nAmount of compare: ", Counter.merge_compare_count,
          "\nAmount of time to sort:", sort_time_end)

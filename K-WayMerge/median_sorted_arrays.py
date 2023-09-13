'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

instantiate a heap
create a tuple for each 0th element in each array. (element index, element array)
add the 0th tuple from each given array to the heap
pop off the smallest element of the heap add to "final array"
use the tuple to get the next value indexed value from that array
update the value of the tuple held in heap. ie push the tuple to the heap

repeat until all elements in arrays are exhausted.
find medium index of "final array" if even calculate medium of two middle indexes
return value


'''

import heapq as h


def find_median_sorted_arrays(a: list[int], b: list[int]) -> float:
    tuple_a = (0, a)
    tuple_b = (0, b)

    other_heap = b
    h.heapify(other_heap)
    # my_heap.heappush(tuple_a)

    print(type(other_heap))
    print(other_heap)

    return 0.0


list_a = [2, 3, 3, 4, 5]
list_b = [4, 3, 1, 9, 20]

find_median_sorted_arrays(list_a, list_b)

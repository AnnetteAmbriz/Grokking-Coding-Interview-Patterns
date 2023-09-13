from heapq import *


def k_smallest_number(k: int, lists: list[list]) -> int:
    my_heap = []
    heapify(my_heap)
    results_list = []
    counter = 0
    i = 0

    for a_list in lists:
        heappush(my_heap, (a_list[0], counter, i))
        i += 1

    print("Initial Heap: " + str(my_heap))

    while len(results_list) < k:
        pop = heappop(my_heap)
        results_list.append(pop[0])
        print("Pop: " + str(pop))
        counter = pop[1]
        if len(lists[pop[2]]) > (counter + 1):
            new_push = (lists[pop[2]][counter + 1], pop[1] + 1, pop[2])
            print("Push: " + str(new_push))
            heappush(my_heap, new_push)

    print("Final result: " + str(results_list))

    return results_list[-1]


def merge_n_lists(lists):
    my_heap = []
    heapify(my_heap)

    for a_list in lists:
        for element in a_list:
            heappush(my_heap, element)

    return heappop(my_heap)


my_lists = [[2, 6, 8], [3, 7, 10], [5, 8, 11]]
print(k_smallest_number(3, my_lists))

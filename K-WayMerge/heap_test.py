from heapq import *


def heap_test(li, k):
    print("initial list: " + str(li))
    heapify(li)

    print("The created heap is : ", end="")
    print(list(li))

    # using heappush() to push elements into heap
    # pushes 4
    heappush(li, 4)

    # printing modified heap
    print("The modified heap after push 4 is: ", end="")
    print(list(li))

    # using heappop() to pop smallest element
    print("The popped and smallest element is : ", end="")
    print(heappop(li))
    pass

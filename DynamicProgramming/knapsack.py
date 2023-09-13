def knapsack(values: list[int], weights: list[int], capacity: int) -> int:
    profits_for_capacity = [0] * (capacity + 1)
    profits_capacity_counter = capacity

    for i in range(len(values)):
        profits_capacity_counter = capacity
        while profits_capacity_counter != -1:
            if weights[i] > profits_capacity_counter:
                break
            else:
                current_max = max(profits_for_capacity[profits_capacity_counter], (values[i] + (profits_for_capacity[profits_capacity_counter - weights[i]])))
                profits_for_capacity[profits_capacity_counter] = current_max
                profits_capacity_counter += -1

    return profits_for_capacity[capacity]


def knapsack_1(values: list[int], weights: list[int], capacity: int) -> int:
    capacity_index = []
    for i in range(capacity + 1):
        capacity_index.append(i)
    print(capacity_index)

    max_capacity_grid = [capacity_index]
    print(max_capacity_grid)

    return -1


my_values = [3, 5, 4]
my_weights = [1, 2, 3]
print(knapsack(my_values, my_weights, 3))

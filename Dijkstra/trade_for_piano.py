processed_nodes = []
infinity = float("inf")


def get_lowest_cost_node(my_costs: {}) -> {}:
    lowest_cost = infinity
    lowest_cost_node = None

    for node in my_costs:
        curr_node_cost = my_costs[node]
        if curr_node_cost < lowest_cost and node not in processed_nodes:
            lowest_cost = curr_node_cost
            lowest_cost_node = node
    return lowest_cost_node


def trade_for_piano(items: {}) -> [str]:
    costs = {"A": 6, "B": 2, "Fin": infinity}
    parent = {"A": "Start", "B": "Start", "Fin": None}

    node = get_lowest_cost_node(costs)
    while node is not None:
        curr_cost = costs[node]
        neighbors = items[node]

        print("current node " + str(node))
        print("current cost " + str(curr_cost))
        print("current neighbors " + str(neighbors))

        for n in neighbors.keys():
            new_cost = curr_cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parent[n] = node
        processed_nodes.append(node)
        node = get_lowest_cost_node(costs)

    print("final costs! " + str(costs))
    print("final parents! " + str(parent))
    print("Final shortest path is!? ")

    start = "Start"
    print("Starting from " + start + ": \n")

    children = parent.keys()
    print(children)

    for child in children:
        parent = parent[child]
        print(str(parent) + " -> " + str(child))

    pass


def main():
    test_items = {"Book": {"Rare LP": 5, "Poster": 0},
                  "Poster": {"Bass Guitar": 30, "Drum Set": 35},
                  "Rare LP": {"Bass Guitar": 15, "Drum Set": 20},
                  "Bass Guitar": {"Piano": 20},
                  "Drum Set": {"Piano": 10},
                  "Piano": {}}

    other_test_items = {"Start": {"A": 6, "B": 2},
                        "A": {"Fin": 1},
                        "B": {"A": 3, "Fin": 5},
                        "Fin": {}}

    print("Calling Trading for a piano function: ")
    trade_for_piano(other_test_items)


main()

from collections import deque


def find_mango_seller(name: str) -> bool:
    checked = []
    cue_to_check = deque()
    cue_to_check += (my_graph[name])

    while cue_to_check:
        curr = cue_to_check.popleft()
        print(curr)
        if curr not in checked:
            if "m" == curr:
                print("Found a mango seller!")
                return True
            cue_to_check += my_graph[curr]
            checked.append(curr)

    return False


my_graph = {"you": ["bob", "cain", "deb", "dan"], "bob": ["peter", "tom", "billy"], "cain": ["tom", "you", "m"],
            "deb": [], "dan": [], "peter": [], "tom": [], "billy": []}

find_mango_seller("you")

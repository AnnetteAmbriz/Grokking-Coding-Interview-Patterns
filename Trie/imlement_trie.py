class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children.get(char)
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children.get(char)

        return node.is_word

    def search_prefix(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children.get(char)

        return True


def main():
    test_actions = [["Trie", "insert", "search", "search", "search_prefix", "insert", "search"]]
    test_words = [(), ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    test_trie = Trie()

    # for i in range(len(test_actions)):
    print("Test case ", 1, "\nTrying insert the following word: ",
          test_words[1], "this is the output: ")
    # for action in test_actions[i]:
    # for case in test_words[i]:

    # test_trie.insert(test_words[1])


main()

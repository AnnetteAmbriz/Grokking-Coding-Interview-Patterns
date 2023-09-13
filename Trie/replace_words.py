# Create a trie to store each prefix present in the dictionary.
#
# For each word in the sentence, check whether any initial sequence of characters matches a word in the trie.
#
# Once found, replace the original word in the sentence with the matched prefix.
#
# After processing all the words in the sentence, return the modified sentence
from trie_node import TrieNode
from trie import Trie


def replace_words(sentence: str, prefixes: set) -> str:
    sentence_array = sentence.split(" ")
    final_sentence_array = []
    print("Initial sentence: " + sentence)

    print("Prefixes to modify sentence: " + str(prefixes))
    prefix_tree = Trie()

    for p in prefixes:
        prefix_tree.insert(p)

    for word in sentence_array:
        node = prefix_tree.root

        for i, letter in enumerate(word):
            if letter not in node.children:
                final_sentence_array.append(word)
                break
            node: TrieNode = node.children.get(letter)

            if node.is_word:
                final_sentence_array.append(word[:i + 1])
                break

    final_sentence = " ".join(final_sentence_array)

    print("Final sentence: " + str(final_sentence))
    return final_sentence


test = "where there is a will there is a way"
test_prefixes = {"wi", "wa", "w"}
replace_words(test, test_prefixes)


def replace_full_words(sentence: str, prefixes: set) -> str:
    sentence_array = sentence.split(" ")
    final_sentence_array = []
    print("Initial sentence: " + sentence)

    print("Prefixes to modify sentence: " + str(prefixes))
    prefix_tree = Trie()

    for p in prefixes:
        prefix_tree.insert(p)

    for word in sentence_array:
        curr_word_modify = ""
        node = prefix_tree.root
        for letter in word:
            if letter not in node.children:
                break
            curr_word_modify = curr_word_modify + letter
            node = node.children.get(letter)
        if curr_word_modify == "":
            final_sentence_array.append(word)
        else:
            final_sentence_array.append(curr_word_modify)

    final_sentence = " ".join(final_sentence_array)

    print("Final sentence: " + str(final_sentence))
    return final_sentence


# algo intialize a count array with the 26 0s. initalize a hashmap called grouped_anagrams given an list of words
# iterate over the list and for each word get the ascii value of the letter and place a 1 in the count array index
# valued for the letter when complete, check if the array is a key in the grouped_anagrams hashmap. If yes,
# add the word to the values of that key. else add word and count array as key to the hashmap return grouped_anagrams
# when complete

def group_anagrams(s: list[str]) -> list[list[str]]:
    grouped_anagrams_dic = dict()
    temp_return = [[]]
    curr_letter_count = [0] * 26

    for word in s:
        word_list = list(word)
        for letter in word_list:
            letter.lower()
            letter_value = ord(letter) - ord('a')
            curr_letter_count[letter_value] += 1

        if str(curr_letter_count) in grouped_anagrams_dic.keys():
            str_letter_count = str(curr_letter_count)
            anagram_values = grouped_anagrams_dic.get(str_letter_count)
            print("anagram_values" + str(anagram_values))
            anagram_values.append(word)
            grouped_anagrams_dic.update({str(curr_letter_count): anagram_values})
            curr_letter_count = [0] * 26
        else:
            grouped_anagrams_dic.update({str(curr_letter_count): [word]})
            curr_letter_count = [0] * 26

    result = list(grouped_anagrams_dic.values())
    return result


def main():
    test_cases = [["first", "second", "tsrif"], ["deet", "dog", "teed", "cat"]]

    for i in range(len(test_cases)):
        print(i + 1, "\t For following list of words:", test_cases[i], "\n\t these are the anagrams: ",
              "\n\t", group_anagrams(test_cases[i]))
        print("---" * 20)


if __name__ == '__main__':
    main()

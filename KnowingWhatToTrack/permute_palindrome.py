# algo:
# iterate over the string (s)
# check if in hashmap
# if yes, update value, increment by 1
# else, add to hashmap with value 1
# check whether all values in hashmap has no more than 1 odd letter value


def permute_palindrome(s: str) -> bool:
    """
    Function checks whether a given string (s) has a permutation that could create
    a palindrome.

    :param
    s: word str

    :return:
    bool: Returns true if a permutation of (s) could create a palindrome. Else false.
    """
    s_list = list(s)
    letter_count = dict()
    print("letter list: " + str(s_list))

    for i in range(len(s_list)):
        if s_list[i] in letter_count.keys():
            updated_value = letter_count.get(s_list[i]) + 1
            letter_count.update({s_list[i]: updated_value})
        else:
            letter_count.update({s_list[i]: 1})

    odd_count = 0
    for i in letter_count.values():
        if i % 2 >= 1:
            odd_count += 1

    if odd_count > 1:
        return False

    print("final letter count hashmap: " + str(letter_count))

    return True


def main():
    test_cases = ["baab", "test", "", "radar", "abb", "racecar"]

    for i in range(len(test_cases)):
        print(i + 1, "\t Could the string:", test_cases[i],
              "be a palindrome? ",
              f"\n\t",
              permute_palindrome(test_cases[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()

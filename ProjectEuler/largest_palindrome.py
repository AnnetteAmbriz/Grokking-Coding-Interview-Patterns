def largest_palindrome(num: int) -> int:
    starting_digit = [9] * num
    print(starting_digit)

    return 0


def main():
    test_cases = [2, 3]

    for i in range(len(test_cases)):
        print(i + 1, "\t The largest palindromic number made "
                     "from the products of", test_cases[i], ",", test_cases[i],
              "digit numbers is:",
              largest_palindrome(test_cases[i]))
        print("---" * 20)


if __name__ == '__main__':
    main()

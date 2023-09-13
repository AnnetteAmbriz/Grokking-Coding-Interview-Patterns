def find_multiples(nums: list[int], maximum: int) -> int:
    sum_of_multiples = 0
    multiples_set = set()

    def calculate_multiples(number: int, m: int) -> list[int]:
        total = 0
        count = 1
        multiples = []

        while total < m:
            total = number * count
            if total < m:
                multiples.append(number * count)
            count += 1

        return multiples

    for num in nums:
        calculated_multiples = calculate_multiples(num, maximum)

        for multiple in calculated_multiples:
            multiples_set.add(multiple)

    for num in multiples_set:
        sum_of_multiples += num

    return sum_of_multiples


def main():
    test_cases = [[3, 5], [3, 5]]

    test_max = [10, 1000]

    for i in range(len(test_cases)):
        print(i + 1, "\t For the list of integers: ", test_cases[i],
              "\n\t The sum of all their multiples below", test_max[i], "is:",
              "\n\t", find_multiples(test_cases[i], test_max[i]))

        print("---" * 20)


if __name__ == '__main__':
    main()

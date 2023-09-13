# Find repeated sequences in a string (s) that represents a DNA sequence of a given length k

def find_repeated_sequences(s: str, k: int) -> set:
    a, b = 0, k
    output_set = set()
    dna_hashes = []
    s_list = list(s)

    for i in range(len(s)):
        curr_hash = s_list[a:k]

        if curr_hash in dna_hashes:
            curr_hash_str = ''.join(map(str, curr_hash))
            output_set.add(curr_hash_str)
        else:
            dna_hashes.append(curr_hash)
        a += 1
        k += 1

    return output_set


def main():
    test_cases = ["AGCTGAAAGCTTAGCTG",
                  "AAAAACCCCCAAAAACCCCCC",
                  "GGGGGGGGGGGGGGGGGGGGGGGGG",
                  "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT",
                  "AAAAAACCCCCCCAAAAAAAACCCCCCCTG",
                  "ATATATATATATATAT"]

    k = [5, 8, 12, 10, 10, 6]

    # loop to execute till the length of list k
    for i in range(len(k)):
        print(i + 1, ".\t DNA Sequence: ", test_cases[i],
              f"\n\t K = {k[i]}",
              f"\n\t Subsequence(s) for the given DNA string are: ",
              find_repeated_sequences(test_cases[i], k[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()

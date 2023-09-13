# function takes in a sentence (s) as a string and returns a dictionary with the word count of
# each word in the sentence
import typing


def word_count(s: str) -> typing.Dict[str, int]:
    s_lower = s.lower()
    s_strip = s_lower.strip(".!")

    s_list = s_strip.split(" ")
    word_counts = dict()

    for i in s_list:
        if i in word_counts.keys():
            new_value = word_counts.get(i) + 1
            word_counts.update({i: new_value})
        else:
            word_counts.update({i: 1})

    return word_counts


# driver code
def main():
    test_cases = ["David is Angry and Martha is also! angry.", ""]

    for i in range(len(test_cases)):
        print(i + 1, "\t For the sentence:", test_cases[i],
              f"\n\t These are the following word(s) and counts:",
              word_count(test_cases[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()

def justify_words(words, k):
    op_list = []
    line = []
    chars_length = 0
    overspill_chars_length = 0

    for word in words:
        chars_length += len(word) + 1

        if chars_length < (k + 1):
            line.append(word)
            border_word = ""
        else:
            border_word = word
            overspill_chars_length = chars_length
            chars_length = len(border_word)
            line = []

        print(chars_length, overspill_chars_length)
        if border_word:
            overspill_chars_length = 0
            line.append(border_word)

        op_list.append(line)

    return op_list


if __name__ == '__main__':
    input_k = 16
    input_list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

    result = justify_words(input_list, input_k)
    print(result)

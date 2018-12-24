def get_words(ip_string, ip_words):
    op_list = []

    for word in ip_words:
        if word in ip_string:
            op_list.append(word)

    return op_list


if __name__ == '__main__':
    input_string = "bedbathandbeyond"
    input_words = ['bed', 'bath', 'bedbath', 'and', 'beyond']

    result = get_words(input_string, input_words)
    print(result)

def str_encoding(ip_string):
    op_string = ""
    count = 1

    for i, chara in enumerate(ip_string):
        if i < len(ip_string)-1:
            if chara == ip_string[i+1]:
                count += 1
            else:
                op_string += str(count) + chara
                count = 1
    op_string += str(count) + chara

    return op_string


if __name__ == '__main__':
    input_string = "AAAABBBCCDAA"

    result = str_encoding(input_string)
    print(result)

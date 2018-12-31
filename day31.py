def get_edit_distance(str1, str2):
    abs_difference = abs(len(str1) - len(str2))

    substitutions = 0
    for (char_x, char_y) in zip(str1, str2):
        if char_x != char_y:
            substitutions += 1

    return abs_difference + substitutions


if __name__ == '__main__':
    string1 = "kitten"
    string2 = "sitting"

    result = get_edit_distance(string1, string2)
    print(result)

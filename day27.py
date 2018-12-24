def is_parenthesis_valid(ip_string):
    testing_stack = []

    for char in ip_string:
        if char == ')':
            if testing_stack[len(testing_stack) - 1] == '(':
                testing_stack.pop()
        elif char == ']':
            if testing_stack[len(testing_stack) - 1] == '[':
                testing_stack.pop()
        else:
            testing_stack.append(char)

    if testing_stack:
        return False
    else:
        return True


if __name__ == '__main__':
    input_string1 = "([)]"
    input_string2 = "((()"
    input_string3 = "([])"
    input_string4 = "(())"

    result1 = is_parenthesis_valid(input_string1)
    result2 = is_parenthesis_valid(input_string2)
    result3 = is_parenthesis_valid(input_string3)
    result4 = is_parenthesis_valid(input_string4)
    print(result1, result2, result3, result4)

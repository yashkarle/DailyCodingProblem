def do_add_up(inp_list, k):
    s = set()
    for n in inp_list:
        if k - n in s:
            print(n, s)
            return True
        s.add(n)

    print(s)
    return False


if __name__ == '__main__':
    input_list = [10, 11, 3, 8]
    k = 17

    result = do_add_up(input_list, k)
    print(result)

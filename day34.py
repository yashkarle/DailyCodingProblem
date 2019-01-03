def get_min_palindrome(ip_str, low, high):
    int_max = 9999

    # base conditions
    # we cross pointers
    if low > high:
        return int_max
    # if only single character
    if low == high:
        return 0
    # if only two characters
    if low == high - 1:
        return 0 if ip_str[low] == ip_str[high] else 1

    # final evaluation
    return get_min_palindrome(ip_str, low + 1, high - 1) if ip_str[low] == ip_str[high] \
        else min(get_min_palindrome(ip_str, low, high - 1), get_min_palindrome(ip_str, low + 1, high)) + 1


if __name__ == '__main__':
    input_str1 = "geeks"
    input_str2 = "google"
    input_str3 = "rare"
    input_str4 = "race"

    result = get_min_palindrome(input_str1, 0, len(input_str1) - 1)
    print(result)

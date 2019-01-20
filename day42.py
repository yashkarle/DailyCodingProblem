def is_subset_sum(ip_set, n, ip_sum):
    # Base Cases
    if ip_sum == 0:
        return True
    if n == 0 and ip_sum != 0:
        return False

    # If last element is greater than
    # sum, then ignore it
    if ip_set[n - 1] > ip_sum:
        return is_subset_sum(ip_set, n - 1, ip_sum)

    # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return is_subset_sum(ip_set, n - 1, ip_sum) or is_subset_sum(ip_set, n - 1, ip_sum - ip_set[n - 1])


if __name__ == '__main__':
    input_list = [12, 1, 61, 5, 9, 2]
    ip_k = 24

    result = is_subset_sum(input_list, len(input_list), ip_k)
    print(result)

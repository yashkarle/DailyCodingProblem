def get_itinerary(ip_list, start):
    ip_len = len(ip_list)
    each_tuple = ()
    itinerary = []

    i = 0
    while i < ip_len:
        for each_tuple in ip_list:
            if each_tuple[0] == start:
                start = each_tuple[1]
                itinerary.append(each_tuple[0])
                ip_list.remove(each_tuple)
        i += 1

    itinerary.append(each_tuple[1])

    if len(itinerary) == 2:
        return []
    else:
        return itinerary


if __name__ == '__main__':
    ip_list1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    start1 = 'YUL'

    ip_list2 = [('SFO', 'COM'), ('COM', 'YYZ')]
    start2 = 'COM'

    ip_list3 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
    start3 = 'A'

    result = get_itinerary(ip_list3, start3)
    print(result)

def missing_number(num_list):
    sort_list = sorted(num_list)

    for each_num in range(len(sort_list)):
        if each_num < len(sort_list):
            if sort_list[each_num + 1] != sort_list[each_num] + 1:
                return sort_list[each_num] + 1
    return None

number_list = [8, 5, 4, 1, 2, 3, 0, 7]
print(missing_number(number_list))

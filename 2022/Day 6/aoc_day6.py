lst = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
lst = list(lst)


def sliding_window(elements, window_size):

    list_of_lists = []
    closest_to_marker = 0

    if len(elements) <= window_size:
        return elements

    for i in range(len(elements) - window_size + 1):
        current_window = elements[i : i + window_size]
        list_of_lists.append(current_window)

    for n in list_of_lists:
        if len(set(n)) == len(n):
            closest_to_marker = list_of_lists.index(n)
            break

    marker = list_of_lists[closest_to_marker + 1][0]

    return list_of_lists, closest_to_marker, marker


print(sliding_window(lst, 4))

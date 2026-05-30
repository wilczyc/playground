from simple_term_menu import TerminalMenu

def merge_sort(_data, reverse):
    print(f"Input array: {_data}")
    arr = list(_data)

    def _merge_sort(lst):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        sorted_left = _merge_sort(left_half)
        sorted_right = _merge_sort(right_half)

        merged = []
        i = j = 0

        while i < len(sorted_left) and j < len(sorted_right):
            # Check mode and sort
            if (sorted_left[i] >= sorted_right[j]) if reverse else (sorted_left[i] <= sorted_right[j]):
                merged.append(sorted_left[i])
                i += 1
            else:
                merged.append(sorted_right[j])
                j += 1

        while i < len(sorted_left):
            merged.append(sorted_left[i])
            i += 1

        while j < len(sorted_right):
            merged.append(sorted_right[j])
            j += 1

        return merged

    sorted_arr = _merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    return sorted_arr

def merge_sort_len(_data):
    ##TODO: FIX
    print(f"Input array: {_data}")
    arr = list(_data)

    def _merge_sort(lst):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        sorted_left = _merge_sort(left_half)
        sorted_right = _merge_sort(right_half)
        print(f"DEBUG: {left_half}, {right_half}, {sorted_left}, {sorted_right}")


        merged = []
        i = j = 0

        while i < len(sorted_left) and j < len(sorted_right):
            # Check mode and sort
            print(f"DEBUG: {sorted_left[i]}, {sorted_right[j]}")
            if sorted_left[i].length() >= sorted_right[j].length():
                merged.append(sorted_left[i])
                i += 1
            else:
                merged.append(sorted_right[j])
                j += 1

        while i < len(sorted_left):
            merged.append(sorted_left[i])
            i += 1

        while j < len(sorted_right):
            merged.append(sorted_right[j])
            j += 1

        return merged

    sorted_arr = _merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    return sorted_arr


def prepare_data(mode):
    if mode == 1 or mode == 2:
        integer_list = [432, 1, 54, 323]
        return integer_list
    elif mode == 3:
        float_list = [3.14, 1, 54, 323]
        return float_list
    elif mode == 4:
        string_list = ["tomato", "potato", "list", "python"]
        return string_list
    elif mode == 5:
        string_list = ["tomato", "potato", "List", "Python"]
        return string_list
    elif mode == 6:
        string_list_extra = ["123456", "123", "12345678", "1234", "1", "00"]
        return string_list_extra
    return None

##################################################################
examples = ["01: Sort a small list of integers.",
           "02: Sort in descending order (use reverse=True).",
           "03: Sort a list of floats.",
           "04: Sort strings alphabetically.",
           "05: Case-insensitive string sort (key=str.lower).",
           "06: Sort strings by length (key=len)"]
menu = TerminalMenu(examples, title="Merge sort - 30 easier practice questions:")
user_choice = menu.show()
mode = user_choice + 1
print(f"Example chosen: {examples[user_choice]}")


if mode == 2:
    data = prepare_data(mode)
    merge_sort(data, True)
if mode == 6:
    data = prepare_data(mode)
    merge_sort_len(data)
else:
    data = prepare_data(mode)
    merge_sort(data, False)



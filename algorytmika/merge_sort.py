def merge_sort(data):
    arr = list(data)

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
            if sorted_left[i] <= sorted_right[j]:
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

merge_sort([3, 100, 1, 44, 12])
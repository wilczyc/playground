def bubble_sort_swap(data):
    n = len(data)
    for i in range (n-1):
        swapped = False
        for j in range (n - i - 1):
            left = data[j]
            right = data[j + 1]
            if left > right:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break
    print(data)

bubble_sort_swap([23,1,56,44,12])
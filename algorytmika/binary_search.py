def binary_search(data, target):
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            print("Wartosc znaleziona!")
            return mid
        elif data[mid] < target:
            left = mid + 1
            print(f"Pudlo, mid ({data[mid]} < {target}. Nowe wartosci:")
            print(f"Left: {left}, Mid: {mid}, Right: {right}")
        else:
            right = mid - 1
            print(f"Pudlo, mid ({data[mid]} > {target}. Nowe wartosci:")
            print(f"Left: {left}, Mid: {mid}, Right: {right}")

    # Nie znaleziono
    return -1

####
data = [11, 12, 22, 25, 34, 64, 90]
target = 34

result = binary_search(data, target)

print(f"Lista: {data}")
print(f"Szukana wartość ({target}) znaleziona na indeksie: {result}")
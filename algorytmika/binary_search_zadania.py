from simple_term_menu import TerminalMenu

def binary_search(_data, _target):
    left, right = 0, len(_data) - 1

    while left <= right:
        mid = (left + right) // 2
        if _data[mid] == _target:
            return mid
        elif _data[mid] < _target:
            left = mid + 1
        else:
            right = mid - 1

    # Nie znaleziono
    return -1

def first_occurence(_data, _target):
    left, right = 0, len(_data) - 1
    last_found_target_index = -1

    while left <= right:
        mid = (left + right) // 2
        if _data[mid] == _target:
            last_found_target_index = mid
            right = mid - 1
        elif _data[mid] < _target:
            left = mid + 1
        else:
            right = mid - 1

    # Zwroc ostatni znaleziony indeks
    return last_found_target_index

def last_occurence(_data, _target):
    left, right = 0, len(_data) - 1
    last_found_target_index = -1

    while left <= right:
        mid = (left + right) // 2
        if _data[mid] == _target:
            last_found_target_index = mid
            left = mid + 1
        elif _data[mid] < _target:
            left = mid + 1
        else:
            right = mid - 1

    # Zwroc ostatni znaleziony indeks
    return last_found_target_index

def count_occurences(_data, _target):
    index_pierwszego_powtorzenia = first_occurence(_data, _target)
    index_ostatniego_powtorzenia = last_occurence(_data, _target)
    ilosc_powtorzen = index_ostatniego_powtorzenia - index_pierwszego_powtorzenia + 1
    return ilosc_powtorzen

def next_greater(_data, _target):
    left, right = 0, len(_data) - 1
    last_valid_value = -1

    while left <= right:
        mid = (left + right) // 2
        if _data[mid] == _target:
            last_found_target_index = mid
            break
        elif _data[mid] < _target:
            left = mid + 1
            # Sprawdz czy na nastepnym indeksie bedzie duplikat
            last_valid_value = _data[mid]

            # Jesli nie: zwroc nastepny indeks
        else:
            right = mid - 1

    # Zwroc ostatni znaleziony indeks
    return last_valid_value

####################
## Wybierałka
zadania = ["01: Find the index of value 25 in the array.",
           "02: Search for an element not in the array.",
           "03: First occurence in duplicates.",
           "04: Last occurence in duplicates.",
           "05: Count occurences of duplicates.",
           "06: Find index of smallest element greater than target"]
menu = TerminalMenu(zadania, title="Zadania wykorzystujące binary search. Wybierz zadanie:")
wybor = menu.show()
mode = wybor + 1
print(f"Wybrano zadanie {zadania[wybor]}")

## Odpalenie funkcji:
match mode:
    case 1:
        data = [11, 12, 22, 25, 34, 64, 90]
        target = 25
        result = binary_search(data, target)
    case 2:
        data = [10, 20, 30, 40, 60]
        target = 50
        result = binary_search(data, target)
    case 3:
        data = [1, 2, 2, 2, 3]
        target = 2
        result = first_occurence(data, target)
    case 4:
        data = [1, 2, 2, 2, 3]
        target = 2
        result = last_occurence(data, target)
    case 5:
        data = [1, 2, 2, 2, 3]
        target = 2
        result = count_occurences(data, target)
    case 6:
        data = [10, 20, 30, 40]
        target = 25
        result = next_greater(data, target)
    case _:
        print("Nieznany tryb!")

## Printout:
print(f"\n\nLista: {data}")
if mode == 5:
    print(f"Ilość powtórzeń wartości ({target}) to: {result}")
elif mode == 6:
    print(f"Najblizsza, wieksza wartosc od szukanej to: {result}")
else:
    if result != -1:
        print(f"Szukana wartość ({target}) znaleziona na indeksie: {result}")
    else:
        print(f"Szukana wartość ({target}) nie została znaleziona!")

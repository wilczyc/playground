def minimal_bubble_sort(data):
    data_orig = data.copy()
    liczba_petli = 0
    print(f"\n######\nDane przed sortowaniem: {data} \n######\n")
    n = len (data)
    for i in range (n-1):
        liczba_petli += 1
        print(f"Poczatek petli {i+1}")
        swapped = False
        for j in range (n-i-1):
            left = data[j]
            right = data[j+1]

            if left > right:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                print(f"Iteracja {j+1}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                print(f"    Nowy wektor: {data}")
            else:
                print(f"Iteracja {j+1}: porownanie {left} i {right}. Nie zamieniono elementów pary")
        if not swapped:
            print(f"Nie zamieniono wartosci, wychodzenie z petli.")
            break
        print(f"Dane na koniec petli {i+1}: {data}")
        print()
    print(f"\n##################\nDane przed sortowaniem: {data_orig}\nDane po sortowaniu:     {data} \n"
          f"Ilosc potrzebnych iteracji głównej pętli: {liczba_petli}\n##################")

def cocktail_shaker_sort(data):
    data_orig = data.copy()
    liczba_petli = 0
    liczba_iteracji_w_petli = 0
    print(f"\n######\nDane przed sortowaniem: {data} \n######\n")
    n = len(data)
    for i in range(n - 1):
        liczba_petli += 1
        liczba_iteracji_w_petli = 0
        print(f"Poczatek petli {i + 1}")
        swapped = False

        # Petla od lewej do prawej
        for j in range(n - i - 1):
            liczba_iteracji_w_petli += 1
            left = data[j]
            right = data[j + 1]

            if left > right:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                print(f"Iteracja {liczba_iteracji_w_petli}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                print(f"    Nowy wektor: {data}")
            else:
                print(f"Iteracja {liczba_iteracji_w_petli}: porownanie {left} i {right}. Nie zamieniono elementów pary")

        # Petla od prawej do lewej
        for j in range (n - i -1, i, -1):
            liczba_iteracji_w_petli += 1
            left = data[j-1]
            right = data[j]

            if left > right:
                data[j - 1], data[j] = data[j], data[j - 1]
                swapped = True
                print(f"Iteracja {liczba_iteracji_w_petli}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                print(f"    Nowy wektor: {data}")
            else:
                print(f"Iteracja {liczba_iteracji_w_petli}: porownanie {left} i {right}. Nie zamieniono elementów pary")

        if not swapped:
            print(f"Nie zamieniono wartosci, wychodzenie z petli.")
            break
        print(f"Dane na koniec petli {i + 1}: {data}")
        print()
    print(f"\n##################\nDane przed sortowaniem: {data_orig}\nDane po sortowaniu:     {data} \n"
          f"Ilosc potrzebnych iteracji głównej pętli: {liczba_petli}\n##################")

def sort_by_two_keys(data):
    data_orig = data.copy()
    liczba_petli = 0
    print(f"\n######\nDane przed sortowaniem: {data} \n######\n")
    n = len(data)
    for i in range(n - 1):
        liczba_petli += 1
        print(f"Poczatek petli {i + 1}")
        swapped = False

        # Petla od lewej do prawej
        for j in range(n - i - 1):
            left = data[j][1]
            right = data[j + 1][1]

            # Porownaj nazwiska i sortuj
            if left > right:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                print(f"Iteracja {j + 1}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                print(f"    Nowy wektor: {data}")
            # Jesli nazwiska sa takie same, sprawdz imiona
            elif left == right:
                left_name = data[j][0]
                right_name = data[j+1][0]
                if left_name > right_name:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    print(f"Iteracja {j + 1}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                    print(f"    Nowy wektor: {data}")
                    swapped = True
            else:
                print(f"Iteracja {j + 1}: porownanie {left} i {right}. Nie zamieniono elementów pary")

        if not swapped:
            print(f"Nie zamieniono wartosci, wychodzenie z petli.")
            break
        print(f"Dane na koniec petli {i + 1}: {data}")
        print()

    print(f"\n##################\nDane przed sortowaniem: {data_orig}\nDane po sortowaniu:     {data} \n"
          f"Ilosc potrzebnych iteracji głównej pętli: {liczba_petli}\n##################")

def bubble_sort_count_comparisons(data):
    data_orig = data.copy()
    liczba_petli = 0
    ilosc_porownan = 0
    ilosc_zamian = 0
    print(f"\n######\nDane przed sortowaniem: {data} \n######\n")
    n = len (data)
    for i in range (n-1):
        liczba_petli += 1
        print(f"Poczatek petli {i+1}")
        swapped = False
        for j in range (n-i-1):
            ilosc_porownan += 1
            left = data[j]
            right = data[j+1]

            if left > right:
                ilosc_zamian += 1
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                print(f"Iteracja {j+1}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                print(f"    Nowy wektor: {data}")
            else:
                print(f"Iteracja {j+1}: porownanie {left} i {right}. Nie zamieniono elementów pary")
        if not swapped:
            print(f"Nie zamieniono wartosci, wychodzenie z petli.")
            break
        print(f"Dane na koniec petli {i+1}: {data}")
        print()
    print(f"\n##################\nDane przed sortowaniem: {data_orig}\nDane po sortowaniu:     {data}\n\n"
          f"Ilosc potrzebnych iteracji głównej pętli: {liczba_petli}\n"
          f"Ilosc dokonanych porownan: {ilosc_porownan}\n"
          f"Ilosc dokonanych zamian: {ilosc_zamian}\n##################")

def bubble_sort_k_passes(data, maksymalna_liczba_petli):
    data_orig = data.copy()
    wasInterrupted = False
    liczba_petli = 0
    print(f"\n######\nDane przed sortowaniem: {data} \n######\n")
    n = len (data)
    for i in range (n-1):
        liczba_petli += 1
        print(f"Poczatek petli {i+1}")
        swapped = False
        for j in range (n-i-1):
            left = data[j]
            right = data[j+1]

            if left > right:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                print(f"Iteracja {j+1}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                print(f"    Nowy wektor: {data}")
            else:
                print(f"Iteracja {j+1}: porownanie {left} i {right}. Nie zamieniono elementów pary")
        if not swapped:
            print(f"Nie zamieniono wartosci, wychodzenie z petli.")
            break
        print(f"Dane na koniec petli {i+1}: {data}")
        print()
        if liczba_petli + 1 > maksymalna_liczba_petli:
            print(f"Maksymalna liczba petli ({maksymalna_liczba_petli}) osiagnieta!")
            wasInterrupted = True
            break
    print(f"\n##################\n"
          f"Dane przed sortowaniem: {data_orig}\n"
          f"Dane po sortowaniu:     {data}\n")

    if wasInterrupted:
              print(f"Sortowanie niekompletne. Zatrzymano na iteracji: {liczba_petli}\n"
              f"##################")
    else:
        print(f"Ilosc potrzebnych iteracji głównej pętli: {liczba_petli}\n"
              f"##################")

def bubble_sort_with_log(data):
    data_orig = data.copy()
    liczba_petli = 0
    ilosc_porownan = 0
    ilosc_zamian = 0
    print(f"\n######\nDane przed sortowaniem: {data} \n######\n")
    n = len (data)
    for i in range (n-1):
        liczba_petli += 1
        print(f"Poczatek petli {i+1}")
        swapped = False
        for j in range (n-i-1):
            ilosc_porownan += 1
            left = data[j]
            right = data[j+1]

            if left > right:
                ilosc_zamian += 1
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                print(f"Iteracja {j+1}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                print(f"    Nowy wektor: {data}")
            else:
                print(f"Iteracja {j+1}: porownanie {left} i {right}. Nie zamieniono elementów pary")
        if not swapped:
            print(f"Nie zamieniono wartosci, wychodzenie z petli.")
            break
        print(f"Dane na koniec petli {i+1}: {data}")
        print()
    print(f"\n##################\nDane przed sortowaniem: {data_orig}\nDane po sortowaniu:     {data}\n\n"
          f"Ilosc potrzebnych iteracji głównej pętli: {liczba_petli}\n"
          f"Ilosc dokonanych porownan: {ilosc_porownan}\n"
          f"Ilosc dokonanych zamian: {ilosc_zamian}\n##################")
    return data, swap_log

##################################################################
print("Sortowanie babelkowe. Wybierz zadanie:")
print("  1> Minimal bubble sort.")
print("  2> Bidirectional bubble sort.")
print("  3> Sort by two keys (last name, then first name).")
print("  4> Bubble sort count comparisons.")
print("  5> Bubble sort that stops after k passes.")
print("  6> Bubble sort that returns a swap log. [INCOMPLETE]")
mode = int(input(">> "))
if (mode < 1) or (mode > 6):
    print("Nieprawidlowy input, kontynuuje w trybie 1.\n")
    mode = 1

# print("Podaj wektor danych do sortowania oddzielony spacjami:")
# data = [int(x) for x in input(">> ").split()]

data = [5, 23, 6, 549, 0, 543, 9823]
passess_amount = 3
data_list_of_tuples = [("John", "Smith"), ("Alice", "Brown"), ("Bob", "Smith"), ("Charlie", "Adams")]

if mode == 1:
    minimal_bubble_sort(data)
elif mode == 2:
    cocktail_shaker_sort(data)
elif mode == 3:
    sort_by_two_keys(data_list_of_tuples)
elif mode == 4:
    bubble_sort_count_comparisons(data)
elif mode == 5:
    bubble_sort_k_passes(data, passess_amount)
elif mode == 6:
    sorted_a, swap_log = bubble_sort_with_log(data)
    print(sorted_a)
    print("#swaps:", len(swap_log))
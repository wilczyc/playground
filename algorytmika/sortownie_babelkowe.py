def bubble_sort(data):
    liczba_petli = 0
    print(f"\n##################\nDane przed sortowaniem: {data} \n##################\n")
    n = len (data)
    for i in range (n-1):
        liczba_petli += 1
        if mode %2 == 0:
            print(f"Poczatek petli {i+1}")
        for j in range (n-i-1):
            left = data[j]
            right = data[j+1]

            if left > right:
                data[j], data[j+1] = data[j+1], data[j]
                if mode % 2 == 0:
                    print(f"Iteracja {j+1}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                    print(f"    Nowy wektor: {data}")
            else:
                if mode % 2 == 0:
                    print(f"Iteracja {j+1}: Porownanie {left} i {right}. Nie zamieniono elementów pary")
        if mode %2 == 0:
            print(f"Dane na koniec petli {i+1}: {data}")
            print()
    print(f"##################\nDane po sortowaniu: {data} \n"
          f"Ilosc potrzebnych iteracji głównej pętli: {liczba_petli}\n##################")

def bubble_sort_swap(data):
    liczba_petli = 0
    print(f"\n######\nDane przed sortowaniem: {data} \n######\n")
    n = len (data)
    for i in range (n-1):
        liczba_petli += 1
        if mode %2 == 0:
            print(f"Poczatek petli {i+1}")
        swapped = False
        for j in range (n-i-1):
            left = data[j]
            right = data[j+1]

            if left > right:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                if mode % 2 == 0:
                   print(f"Iteracja {j+1}: Porownanie {left} i {right}. Zamieniono kolejność na {right} {left}")
                   print(f"    Nowy wektor: {data}")

            else:
                if mode % 2 == 0:
                    print(f"Iteracja {j+1}: porownanie {left} i {right}. Nie zamieniono elementów pary")
        if not swapped:
            print(f"Nie zamieniono wartosci, wychodzenie z petli.")
            break
        if mode %2 == 0:
            print(f"Dane na koniec petli {i+1}: {data}")
            print()
    print(f"\n##################\nDane po sortowaniu: {data} \n"
          f"Ilosc potrzebnych iteracji głównej pętli: {liczba_petli}\n##################")

print("Sortowanie babelkowe. Wybierz zadanie:")
print("  1> Klasyczne sortowanie babelkowe.")
print("  2> Klasyczne sortowanie babelkowe z opisem akcji.")
print("  3> Sortowanie babelkowe z flagą swap")
print("  4> Sortowanie babelkowe z flagą swap i opisem")
mode = int(input(">> "))
if (mode < 1) or (mode > 4):
    print("Nieprawidlowy input, kontynuuje w trybie 1.\n")
    mode = 1

print("Podaj wektor danych do sortowania oddzielony spacjami:")
data = [int(x) for x in input(">> ").split()]
if mode == 1 or mode == 2:
    bubble_sort(data)
elif mode == 3 or mode == 4:
    bubble_sort_swap(data)


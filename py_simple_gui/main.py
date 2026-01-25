import PySimpleGUI as sg

tab1_layout = [[sg.Text("Program wyświetla liczbę parzystych liczb od 0 do podanej przez użytkownika liczby.")],
               [sg.Text("Podaj liczbę:")],
               [sg.InputText(key='input1', size=(8, 1))],
               [sg.Button('Oblicz', key='tab1_action')],
               [sg.Text('', key='wynik1', size=(50, 2))]]

tab2_layout = [[sg.Text("Program pozwala użytkownikowi podać różne typy danych, po czym filtruje tylko liczby.")],
               [sg.Text("Podaj wartość do przefiltrowania:")],
               [sg.InputText(key='input2', size=(12, 1))],
               [sg.Button('Filtruj', key='tab2_action')],
               [sg.Text('', key='wynik2', size=(50, 2))]]

# tab2_layout = [
#     [sg.Frame('Główny Frame', [
#         [sg.Frame('Podframe 1', [
#             [sg.Text('Treść w podframe 1')],
#             [sg.InputText(key='input_sub1')]
#         ])],
#         [sg.Frame('Podframe 2', [
#             [sg.Text('Treść w podframe 2')],
#             [sg.InputText(key='input_sub2')]
#         ])]
#     ])],
#     [sg.Button('Wyślij', key='wyslij2')],
#     [sg.Text('', key='wynik2', size=(50, 2))]
# ]

layout = [[sg.TabGroup([[sg.Tab('Zadanie 1 - liczby parzyste', tab1_layout),
                         sg.Tab('Zadanie 2 - filtruj elementy liczbowe', tab2_layout)]])],
          [sg.Button('Zamknij ten świetny program', key='close')]]

window = sg.Window('Program', layout, no_titlebar=True, grab_anywhere=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'close':
        break

    if event == 'tab1_action':
        if values['input1'] != '':
            try:
                tab1_input = int(values['input1'])
                tab1_output = (tab1_input // 2)
                window['wynik1'].update(f'Ilość parzystych liczb od 0 do {tab1_input} to {tab1_output}!')
                window['input1'].update('')
            except ValueError:
                window['wynik1'].update('Podaj poprawną liczbę!')

    if event == 'tab2_action':
        if values['input2'] != '':
            try:
                tab2_input = values['input2']
                tab2_input_list = list(tab2_input)
                tab2_output_list = list()
                for element in tab2_input_list:
                    try:
                        liczba = int(element)
                        tab2_output_list.append(liczba)
                    except ValueError:
                        pass
                tab2_output = ''.join(str(x) for x in tab2_output_list)
                window['wynik2'].update(f'Liczby podane przez użytkownika to: {tab2_output}')
                window['input2'].update('')
            except ValueError:
                window['wynik2'].update("Błąd wprowadzenia!")
window.close()
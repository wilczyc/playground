import streamlit as st
import pandas as pd
import numpy as np
import time
import requests
from datetime import datetime
from datetime import date

# Konfiguracja strony
st.set_page_config(
    page_title="Moje Portfolio Programistyczne",
    page_icon="💻",
    layout="wide"
)

# Funkcja do wyświetlania nagłówka
def show_header():
    st.title("💻 Moje Portfolio Programistyczne")
    st.markdown("""
    Witaj w moim portfolio programistycznym! Tutaj prezentuję kilka ciekawych aplikacji napisanych w Pythonie.
    Wybierz jedną z sekcji poniżej, aby zobaczyć konkretne zadanie.
    """)

# Sekcja 1: Kalkulator
def calculator_section():
    st.header("🧮 Kalkulator")
    st.write("Prosty kalkulator do podstawowych operacji matematycznych.")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Pierwsza liczba", value=0.0)
        operation = st.selectbox("Operacja", ["Dodawanie", "Odejmowanie", "Mnożenie", "Dzielenie"])

    with col2:
        num2 = st.number_input("Druga liczba", value=0.0)

    if st.button("Oblicz"):
        if operation == "Dodawanie":
            result = num1 + num2
        elif operation == "Odejmowanie":
            result = num1 - num2
        elif operation == "Mnożenie":
            result = num1 * num2
        elif operation == "Dzielenie":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Nie można dzielić przez zero!")
                return

        st.success(f"Wynik: {result}")

# Sekcja 1b: Kalkulator_tabs
def calculator_2_section():
    st.header("🧮 Kalkulator")
    st.write("Prosty kalkulator do podstawowych operacji matematycznych.")

    dodawanie_tab, odejmowanie_tab, mnozenie_tab, dzielenie_tab = st.tabs(
        ["➕ Dodawanie", "➖ Odejmowanie", "✖️ Mnożenie", "➗ Dzielenie"]
    )

    with dodawanie_tab:
        st.subheader("Dodawanie")
        col1, col2, col3 = st.columns(3)
        with col1:
            num1_add = st.number_input("Pierwsza liczba", value=0.0, key="add1")
        with col2:
            num2_add = st.number_input("Druga liczba", value=0.0, key="add2")
        with col3:
            if st.button("Oblicz", key="btn_add"):
                result = num1_add + num2_add
                st.success(f"Wynik: {num1_add} + {num2_add} = {result}")

    with odejmowanie_tab:
        st.subheader("Odejmowanie")
        col1, col2, col3 = st.columns(3)
        with col1:
            num1_sub = st.number_input("Pierwsza liczba", value=0.0, key="sub1")
        with col2:
            num2_sub = st.number_input("Druga liczba", value=0.0, key="sub2")
        with col3:
            if st.button("Oblicz", key="btn_sub"):
                result = num1_sub - num2_sub
                st.success(f"Wynik: {num1_sub} - {num2_sub} = {result}")

    with mnozenie_tab:
        st.subheader("Mnożenie")
        col1, col2, col3 = st.columns(3)
        with col1:
            num1_mul = st.number_input("Pierwsza liczba", value=0.0, key="mul1")
        with col2:
            num2_mul = st.number_input("Druga liczba", value=0.0, key="mul2")
        with col3:
            if st.button("Oblicz", key="btn_mul"):
                result = num1_mul * num2_mul
                st.success(f"Wynik: {num1_mul} × {num2_mul} = {result}")

    with dzielenie_tab:
        st.subheader("Dzielenie")
        col1, col2, col3 = st.columns(3)
        with col1:
            num1_div = st.number_input("Pierwsza liczba", value=0.0, key="div1")
        with col2:
            num2_div = st.number_input("Druga liczba", value=0.0, key="div2")
        with col3:
            if st.button("Oblicz", key="btn_div"):
                if num2_div != 0:
                    result = num1_div / num2_div
                    st.success(f"Wynik: {num1_div} ÷ {num2_div} = {result}")
                else:
                    st.error("Nie można dzielić przez zero!")

# Sekcja 2: Chatbot
def chatbot_section():
    st.header("💬 Prosty Chatbot")
    st.write("Chatbot, który odpowiada na proste pytania.")

    # Inicjalizacja historii czatu
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Wyświetlenie historii czatu
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Pole do wprowadzania wiadomości
    if prompt := st.chat_input("Napisz coś..."):
        # Dodanie wiadomości użytkownika do historii
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        # Wyświetlenie wiadomości użytkownika
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generowanie odpowiedzi
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            # Prosta logika odpowiedzi
            if "cześć" in prompt.lower() or "witaj" in prompt.lower():
                response = "Cześć! Jak mogę Ci pomóc?"
            elif "jak się masz" in prompt.lower():
                response = "Dziękuję, dobrze! A Ty?"
            elif "data" in prompt.lower():
                response = f"Aktualna data to {datetime.now().strftime('%Y-%m-%d')}"
            else:
                response = "Nie rozumiem tego pytania. Możesz spróbować czegoś innego?"

            # Symulacja pisania odpowiedzi
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        # Dodanie odpowiedzi do historii
        st.session_state.chat_history.append({"role": "assistant", "content": full_response})

# Sekcja 3: Analiza danych
def data_analysis_section():
    st.header("📊 Analiza Danych")
    st.write("Prosta analiza danych z przykładowym zestawem danych.")

    # Generowanie przykładowych danych
    data = pd.DataFrame({
        'Data': pd.date_range(start='2023-01-01', periods=100),
        'Wartość': np.random.randn(100).cumsum(),
        'Kategoria': np.random.choice(['A', 'B', 'C'], 100)
    })

    st.subheader("Przykładowe dane")
    st.dataframe(data.head(10))

    # Wizualizacja danych
    st.subheader("Wizualizacja danych")

    chart_type = st.selectbox("Typ wykresu", ["Liniowy", "Słupkowy", "Punktowy"])

    if chart_type == "Liniowy":
        st.line_chart(data, x='Data', y='Wartość')
    elif chart_type == "Słupkowy":
        st.bar_chart(data, x='Kategoria', y='Wartość')
    elif chart_type == "Punktowy":
        st.scatter_chart(data, x='Data', y='Wartość')

    # Podsumowanie danych
    st.subheader("Podsumowanie danych")
    st.write(data.describe())

    # Filtrowanie danych
    st.subheader("Filtrowanie danych")
    min_date = st.date_input("Data początkowa", data['Data'].min())
    max_date = st.date_input("Data końcowa", data['Data'].max())

    filtered_data = data[(data['Data'] >= pd.to_datetime(min_date)) &
                         (data['Data'] <= pd.to_datetime(max_date))]

    st.write(f"Liczba rekordów: {len(filtered_data)}")
    st.dataframe(filtered_data)

# Sekcja 4: Generator haseł
def password_generator_section():
    st.header("🔑 Generator Haseł")
    st.write("Generator bezpiecznych haseł z różnymi opcjami.")

    length = st.slider("Długość hasła", min_value=8, max_value=32, value=12)
    use_uppercase = st.checkbox("Użyj dużych liter", value=True)
    use_numbers = st.checkbox("Użyj cyfr", value=True)
    use_special = st.checkbox("Użyj znaków specjalnych", value=True)

    if st.button("Wygeneruj hasło"):
        chars = "abcdefghijklmnopqrstuvwxyz"
        if use_uppercase:
            chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if use_numbers:
            chars += "0123456789"
        if use_special:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        password = ''.join(np.random.choice(list(chars), size=length))
        st.success(f"Wygenerowane hasło: {password}")

        # Opcja kopiowania hasła
        if st.button("Kopiuj hasło"):
            st.write("Hasło zostało skopiowane do schowka!")
            st.code(password)

# Sekcja 5: Timer
def timer_section():
    st.header("⏱️ Timer")

    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    if 'paused_time' not in st.session_state:
        st.session_state.paused_time = 0
    if 'is_paused' not in st.session_state:
        st.session_state.is_paused = False
    if 'stop_time' not in st.session_state:
        st.session_state.stop_time = None

    col1, col2 = st.columns(2)
    with col1:
        if not st.session_state.start_time and not st.session_state.is_paused:
            button_label = "Start"
        elif st.session_state.is_paused:
            button_label = "Resume"
        else:
            button_label = "Pause"

        if st.button(button_label):
            if st.session_state.start_time and not st.session_state.is_paused:
                # Pauzowanie
                st.session_state.paused_time += time.time() - st.session_state.start_time
                st.session_state.start_time = None
                st.session_state.is_paused = True
            else:
                # Start/Resume
                st.session_state.start_time = time.time()
                st.session_state.is_paused = False
                st.session_state.stop_time = None
                st.rerun()

    with col2:
        if st.button("Stop"):
            if st.session_state.start_time or st.session_state.is_paused:
                if st.session_state.start_time:
                    st.session_state.paused_time += time.time() - st.session_state.start_time
                st.session_state.stop_time = st.session_state.paused_time
                st.session_state.start_time = None
                st.session_state.paused_time = 0
                st.session_state.is_paused = False

    if st.session_state.stop_time is not None:
        st.success(f"⏹️ Zatrzymano po: {st.session_state.stop_time:.2f}s")

    if st.session_state.start_time and not st.session_state.is_paused:
        elapsed = st.session_state.paused_time + (time.time() - st.session_state.start_time)
        st.metric("Czas", f"{elapsed:.2f}s")
        time.sleep(0.1)
        st.rerun()
    elif st.session_state.is_paused:
        st.metric("Czas (PAUSED)", f"{st.session_state.paused_time:.2f}s")

# Sekcja 6: Formularz
def formularz_section():
    with st.form("my_form"):
        name = st.text_input("Imię")
        age = st.number_input("Wiek", min_value=0)
        submitted = st.form_submit_button("Wyślij")

        if submitted:
            st.write(f"Witaj, {name}! Masz {age} lat.")

# Sekcja 7: Pogoda
def pogoda_section():
    st.header("🌤️ Pogoda")
    st.markdown("Prosty skrypt który ściąga z weather.visualcrossing.com pogodę dla danej daty i wyświetla w czytelnej formie.")
    weather_icons = {
        "clear-day": "☀️",
        "clear-night": "🌙",
        "partly-cloudy-day": "⛅",
        "partly-cloudy-night": "☁️",
        "cloudy": "☁️",
        "rain": "🌧️",
        "snow": "❄️",
        "wind": "💨",
        "fog": "🌫️",
        "sleet": "🌨️",
        "hail": "🧊",
        "thunderstorm": "⛈️"
    }

    city = st.text_input("Miasto", "Warszawa")
    date1 = st.date_input("Data", format="DD/MM/YYYY")

    if st.button("Sprawdź pogodę"):
        api_key = "23V483MZD7NTYTC42QUW2ZL39"
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date1}?key={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            import datetime as dt
            today = dt.date.today()

            if date1 == today and "currentConditions" in data:
                current_conditions = data["currentConditions"]["conditions"]
                current_time = data["currentConditions"]["datetime"]
                current_temp = data["currentConditions"]["temp"]
                current_icon = data["currentConditions"]["icon"]
                icon_emoji = weather_icons.get(current_icon, "🌡️")

                st.subheader("Aktualne warunki:")
                st.write(f"**Godzina:** {current_time}")
                st.write(f"**Warunki:** {icon_emoji} {current_conditions}")

                temp_celc = (current_temp - 32) * 5 / 9
                st.write(f"**Temperatura:** {temp_celc:.1f}°C")
            else:
                day_data = data["days"][0]
                day_icon = day_data.get("icon", "")
                icon_emoji = weather_icons.get(day_icon, "🌡️")

                st.subheader(f"Pogoda dla dnia: {date1.strftime('%d/%m/%Y')}")
                st.write(f"**Warunki:** {icon_emoji} {day_data['conditions']}")
                temp_celc = (day_data['temp'] - 32) * 5 / 9
                st.write(f"**Temperatura średnia:** {temp_celc:.1f}°C")


        except requests.exceptions.RequestException as e:
            st.error(f"Błąd podczas pobierania danych pogodowych: {e}")

        except KeyError as e:
            st.error(f"Błąd w strukturze danych: {e}")

# Sekcja 8: TBD
def TBD():
    st.header("🧮 TBD")
    st.write("TBD.")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Pierwsza liczba", value=0.0)
        operation = st.selectbox("Operacja", ["Dodawanie", "Odejmowanie", "Mnożenie", "Dzielenie"])

    with col2:
        num2 = st.number_input("Druga liczba", value=0.0)

    if st.button("Oblicz"):
        if operation == "Dodawanie":
            result = num1 + num2
        elif operation == "Odejmowanie":
            result = num1 - num2
        elif operation == "Mnożenie":
            result = num1 * num2
        elif operation == "Dzielenie":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Nie można dzielić przez zero!")
                return

        st.success(f"Wynik: {result}")

# Główna funkcja aplikacji
def main():
    show_header()

    # Menu boczne
    with st.sidebar:
        st.header("Menu")
        section = st.radio(
            "Wybierz sekcję:",
            ["🧮 Kalkulator", "🧮 Kalkulator 2", "💬 Chatbot", "📊 Analiza Danych",
             "🔑 Generator Haseł", "⏱Timer", "📝Formularz", "🌤️ Pogoda", "TBD"]
        )

    # Wyświetlanie wybranej sekcji
    if section == "🧮 Kalkulator":
        calculator_section()
    elif section == "🧮 Kalkulator 2":
        calculator_2_section()
    elif section == "💬 Chatbot":
        chatbot_section()
    elif section == "📊 Analiza Danych":
        data_analysis_section()
    elif section == "🔑 Generator Haseł":
        password_generator_section()
    elif section == "⏱Timer":
        timer_section()
    elif section == "📝Formularz":
        formularz_section()
    elif section == "🌤️ Pogoda":
        pogoda_section()
    elif section == "TBD":
        TBD()

    # Informacje o autorze
    st.sidebar.markdown("---")
    st.sidebar.write("Autor: P. Zarnecki & jaaaaa")
    st.sidebar.write("Data: " + datetime.now().strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()
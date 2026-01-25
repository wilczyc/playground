# Portfolio Programistyczne w Pythonie

Aplikacja prezentująca kilka różnych zadań programistycznych w Pythonie z wykorzystaniem Streamlit.

## Funkcje aplikacji

1. **Kalkulator** - Prosty kalkulator do podstawowych operacji matematycznych
2. **Chatbot** - Prosty chatbot do odpowiedzi na pytania
3. **Analiza Danych** - Przykład analizy danych z wizualizacją
4. **Generator Haseł** - Generator bezpiecznych haseł z różnymi opcjami

## Jak uruchomić

1. Sklonuj repozytorium
2. Utwórz wirtualne środowisko:
   ```bash
   python -m venv venv
   
3. aktywuj środowisko:
venv\Scripts\activate
source venv/bin/activate
W zależności oczywiście od systemu
4. Zainstaluj zależności:
pip install -r requirements.txt
5. Uruchom aplikację:
streamlit run app.py

W sumie ciekawym wyzwaniem byłoby rozwinięcie projektu. W związku z tym daję całościowy opis, tutorial:
# Tutorial: Aplikacja Portfolio w Streamlit

## 📋 Spis treści
1. [Wprowadzenie](#wprowadzenie)
2. [Struktura aplikacji](#struktura-aplikacji)
3. [Szczegółowy opis kodu](#szczegółowy-opis-kodu)
4. [Jak rozwijać aplikację](#jak-rozwijać-aplikację)
5. [Najlepsze praktyki](#najlepsze-praktyki)

---

## Wprowadzenie

Ta aplikacja to interaktywne portfolio programistyczne zbudowane w **Streamlit** - frameworku Pythona do tworzenia aplikacji webowych. Streamlit pozwala szybko tworzyć interfejsy użytkownika bez znajomości HTML/CSS/JavaScript.

### Czym jest Streamlit?
- Framework do tworzenia aplikacji webowych w czystym Pythonie
- Automatycznie odświeża aplikację po zmianach w kodzie
- Zawiera gotowe komponenty UI (przyciski, slidery, wykresy)
- Idealny do prototypowania i prezentacji projektów data science

### Wymagania
```bash
pip install streamlit pandas numpy
```

### Uruchamianie aplikacji
```bash
streamlit run nazwa_pliku.py
```

---

## Struktura aplikacji

### 🏗️ Architektura

Aplikacja składa się z kilku kluczowych elementów:

```
┌─────────────────────────────────────┐
│     Konfiguracja strony             │
│  (st.set_page_config)               │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│     Nagłówek aplikacji              │
│  (show_header)                      │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│     Menu boczne (Sidebar)           │
│  - Kalkulator                       │
│  - Chatbot                          │
│  - Analiza Danych                   │
│  - Generator Haseł                  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│     Wybrana sekcja                  │
│  (funkcja odpowiadająca sekcji)     │
└─────────────────────────────────────┘
```

---

## Szczegółowy opis kodu

### 1. Konfiguracja strony

```python
st.set_page_config(
    page_title="Moje Portfolio Programistyczne",
    page_icon="💻",
    layout="wide"
)
```

**Co to robi?**
- `page_title` - tytuł w zakładce przeglądarki
- `page_icon` - ikona (emoji lub URL do obrazka)
- `layout="wide"` - pełna szerokość ekranu (domyślnie: `"centered"`)

**Dlaczego to ważne?**
- Musi być **pierwszym** wywołaniem Streamlit w aplikacji
- Ustawia podstawowe parametry wyglądu
- Wpływa na profesjonalny wygląd aplikacji

---

### 2. Funkcja nagłówka

```python
def show_header():
    st.title("💻 Moje Portfolio Programistyczne")
    st.markdown("""
    Witaj w moim portfolio programistycznym!
    """)
```

**Komponenty Streamlit:**
- `st.title()` - główny tytuł (największa czcionka)
- `st.markdown()` - formatowany tekst (obsługuje Markdown)

**Inne przydatne funkcje tekstowe:**
- `st.header()` - nagłówek sekcji
- `st.subheader()` - podtytuł
- `st.write()` - uniwersalna funkcja do wyświetlania treści
- `st.caption()` - mały tekst pomocniczy

---

### 3. Sekcja Kalkulator

```python
def calculator_section():
    col1, col2 = st.columns(2)
```

**Kluczowe elementy:**

#### Layout w kolumnach
```python
col1, col2 = st.columns(2)  # Dwie równe kolumny
# lub
col1, col2, col3 = st.columns([2, 1, 1])  # Kolumny o różnych szerokościach
```

#### Komponenty wejściowe
```python
num1 = st.number_input("Pierwsza liczba", value=0.0)
operation = st.selectbox("Operacja", ["Dodawanie", "Odejmowanie"])
```

**Dostępne komponenty:**
- `st.number_input()` - pole liczbowe
- `st.text_input()` - pole tekstowe
- `st.selectbox()` - lista rozwijana
- `st.multiselect()` - wielokrotny wybór
- `st.slider()` - suwak
- `st.checkbox()` - pole wyboru
- `st.radio()` - przyciski radio

#### Przyciski i akcje
```python
if st.button("Oblicz"):
    # kod wykonywany po kliknięciu
```

**Ważne:** Kod wewnątrz `if st.button()` wykonuje się **tylko** gdy przycisk jest kliknięty.

#### Wyświetlanie komunikatów
```python
st.success("Wynik: 42")     # Zielony komunikat sukcesu
st.error("Błąd!")           # Czerwony komunikat błędu
st.warning("Uwaga!")        # Żółty komunikat ostrzeżenia
st.info("Informacja")       # Niebieski komunikat informacyjny
```

---

### 4. Sekcja Chatbot

```python
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
```

**Co to jest `st.session_state`?**
- Przechowuje dane między kolejnymi uruchomieniami skryptu
- Streamlit **wykonuje cały kod od nowa** przy każdej interakcji
- `session_state` pozwala zachować stan aplikacji (np. historię czatu)

**Przykład użycia:**
```python
# Inicjalizacja
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Modyfikacja
if st.button("Zwiększ"):
    st.session_state.counter += 1

# Wyświetlanie
st.write(f"Licznik: {st.session_state.counter}")
```

#### Interfejs czatu
```python
if prompt := st.chat_input("Napisz coś..."):
    # prompt zawiera wiadomość użytkownika
```

**Operator walrus `:=`** - przypisuje wartość i zwraca ją jednocześnie.

#### Wyświetlanie wiadomości
```python
with st.chat_message("user"):
    st.markdown(prompt)

with st.chat_message("assistant"):
    st.markdown(response)
```

**Role wiadomości:**
- `"user"` - wiadomość użytkownika (prawa strona)
- `"assistant"` - odpowiedź bota (lewa strona)

#### Efekt pisania
```python
message_placeholder = st.empty()
for chunk in response.split():
    full_response += chunk + " "
    time.sleep(0.05)
    message_placeholder.markdown(full_response + "▌")
```

**`st.empty()`** - tworzy kontener, który można dynamicznie aktualizować.

---

### 5. Sekcja Analiza Danych

```python
data = pd.DataFrame({
    'Data': pd.date_range(start='2023-01-01', periods=100),
    'Wartość': np.random.randn(100).cumsum()
})
```

#### Wyświetlanie danych
```python
st.dataframe(data.head(10))  # Interaktywna tabela
# lub
st.table(data.head(10))      # Statyczna tabela
```

**Różnica:**
- `st.dataframe()` - scrollowanie, sortowanie, pełnoekranowy widok
- `st.table()` - prosty, statyczny wyświetlacz

#### Wykresy
```python
st.line_chart(data, x='Data', y='Wartość')
st.bar_chart(data, x='Kategoria', y='Wartość')
st.scatter_chart(data, x='Data', y='Wartość')
```

**Dostępne wykresy natywne:**
- `st.line_chart()` - wykres liniowy
- `st.bar_chart()` - wykres słupkowy
- `st.area_chart()` - wykres obszarowy
- `st.scatter_chart()` - wykres punktowy

**Zaawansowane wykresy:**
```python
import plotly.express as px

fig = px.line(data, x='Data', y='Wartość', title='Mój wykres')
st.plotly_chart(fig)
```

#### Filtrowanie danych
```python
min_date = st.date_input("Data początkowa", data['Data'].min())
filtered_data = data[data['Data'] >= pd.to_datetime(min_date)]
```

**`st.date_input()`** - wybierak daty z kalendarzem.

---

### 6. Sekcja Generator Haseł

```python
length = st.slider("Długość hasła", min_value=8, max_value=32, value=12)
use_uppercase = st.checkbox("Użyj dużych liter", value=True)
```

#### Generowanie hasła
```python
chars = "abcdefghijklmnopqrstuvwxyz"
if use_uppercase:
    chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ''.join(np.random.choice(list(chars), size=length))
```

#### Wyświetlanie kodu
```python
st.code(password)  # Blok kodu z możliwością kopiowania
```

---

### 7. Menu boczne (Sidebar)

```python
with st.sidebar:
    st.header("Menu")
    section = st.radio("Wybierz sekcję:", ["Kalkulator", "Chatbot"])
```

**`st.sidebar`** - wszystko wewnątrz bloku `with st.sidebar:` pojawia się w bocznym panelu.

**Alternatywna składnia:**
```python
section = st.sidebar.radio("Wybierz sekcję:", [...])
```

---

### 8. Logika routingu

```python
if section == "Kalkulator":
    calculator_section()
elif section == "Chatbot":
    chatbot_section()
```

**Jak to działa?**
1. Użytkownik wybiera opcję w `st.radio()`
2. Wartość zapisuje się w zmiennej `section`
3. Odpowiednia funkcja sekcji jest wywoływana
4. Tylko wybrana sekcja jest renderowana

---

## Jak rozwijać aplikację

### 💡 Pomysły na nowe sekcje

#### 1. **To-Do List**
```python
def todo_section():
    st.header("📝 Lista zadań")
    
    if 'todos' not in st.session_state:
        st.session_state.todos = []
    
    new_todo = st.text_input("Nowe zadanie")
    if st.button("Dodaj"):
        st.session_state.todos.append({"task": new_todo, "done": False})
    
    for i, todo in enumerate(st.session_state.todos):
        col1, col2 = st.columns([4, 1])
        with col1:
            done = st.checkbox(todo["task"], key=f"todo_{i}", value=todo["done"])
            st.session_state.todos[i]["done"] = done
        with col2:
            if st.button("Usuń", key=f"del_{i}"):
                st.session_state.todos.pop(i)
                st.rerun()
```

#### 2. **Konwerter jednostek**
```python
def converter_section():
    st.header("🔄 Konwerter jednostek")
    
    conversion_type = st.selectbox("Typ konwersji", 
                                   ["Temperatura", "Długość", "Waga"])
    
    if conversion_type == "Temperatura":
        value = st.number_input("Wartość")
        from_unit = st.selectbox("Z:", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("Na:", ["Celsius", "Fahrenheit", "Kelvin"])
        
        # Logika konwersji...
```

#### 3. **Timer/Stoper**
```python
def timer_section():
    st.header("⏱️ Timer")
    
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start"):
            st.session_state.start_time = time.time()
    with col2:
        if st.button("Stop"):
            st.session_state.start_time = None
    
    if st.session_state.start_time:
        elapsed = time.time() - st.session_state.start_time
        st.metric("Czas", f"{elapsed:.2f}s")
        time.sleep(0.1)
        st.rerun()
```

#### 4. **Wczytywanie plików**
```python
def file_upload_section():
    st.header("📂 Analiza pliku CSV")
    
    uploaded_file = st.file_uploader("Wybierz plik CSV", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        st.line_chart(df)
```

#### 5. **Kalkulator BMI**
```python
def bmi_calculator():
    st.header("⚖️ Kalkulator BMI")
    
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Waga (kg)", min_value=1.0, value=70.0)
    with col2:
        height = st.number_input("Wzrost (cm)", min_value=1.0, value=170.0)
    
    if st.button("Oblicz BMI"):
        bmi = weight / ((height/100) ** 2)
        st.metric("Twoje BMI", f"{bmi:.2f}")
        
        if bmi < 18.5:
            st.info("Niedowaga")
        elif bmi < 25:
            st.success("Waga prawidłowa")
        elif bmi < 30:
            st.warning("Nadwaga")
        else:
            st.error("Otyłość")
```

---

### 🎨 Ulepszenia wizualne

#### 1. **Motywy kolorystyczne**
```python
# W pliku .streamlit/config.toml
[theme]
primaryColor="#FF4B4B"
backgroundColor="#0E1117"
secondaryBackgroundColor="#262730"
textColor="#FAFAFA"
font="sans serif"
```

#### 2. **Własne style CSS**
```python
st.markdown("""
<style>
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Duży tekst!</p>', unsafe_allow_html=True)
```

#### 3. **Ikony i emotikony**
```python
st.header("📊 Statystyki")
st.metric("Użytkownicy 👥", "1,234", "+12%")
st.metric("Sprzedaż 💰", "5,678 zł", "+23%")
```

#### 4. **Karty informacyjne**
```python
col1, col2, col3 = st.columns(3)
with col1:
    st.info("ℹ️ Informacja")
with col2:
    st.success("✅ Sukces")
with col3:
    st.warning("⚠️ Uwaga")
```

---

### 🚀 Zaawansowane funkcje

#### 1. **Pasek postępu**
```python
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)
st.success("Gotowe!")
```

#### 2. **Spinner podczas ładowania**
```python
with st.spinner("Przetwarzam dane..."):
    time.sleep(3)  # Symulacja długiej operacji
st.success("Gotowe!")
```

#### 3. **Expandery (rozwijane sekcje)**
```python
with st.expander("Kliknij, aby rozwinąć"):
    st.write("Ukryta treść")
    st.image("obraz.jpg")
```

#### 4. **Zakładki (tabs)**
```python
tab1, tab2, tab3 = st.tabs(["📈 Wykres", "📊 Dane", "🔍 Info"])

with tab1:
    st.line_chart(data)
with tab2:
    st.dataframe(data)
with tab3:
    st.write("Informacje o danych")
```

#### 5. **Formularze**
```python
with st.form("my_form"):
    name = st.text_input("Imię")
    age = st.number_input("Wiek", min_value=0)
    submitted = st.form_submit_button("Wyślij")
    
    if submitted:
        st.write(f"Witaj, {name}! Masz {age} lat.")
```

**Dlaczego formularze?**
- Zbierają wszystkie dane przed wysłaniem
- Tylko jeden przycisk "Submit" odświeża aplikację
- Lepsza wydajność przy wielu polach

#### 6. **Cachowanie danych**
```python
@st.cache_data  # Dla danych (DataFrame, listy)
def load_data():
    # Długa operacja wczytywania
    return pd.read_csv("large_file.csv")

@st.cache_resource  # Dla obiektów (połączenia DB, modele ML)
def load_model():
    return load_ml_model()

# Dane wczytają się tylko raz!
data = load_data()
```

---

### 📦 Integracja z zewnętrznymi API

#### Przykład: API pogodowe
```python
import requests

def weather_section():
    st.header("🌤️ Pogoda")
    
    city = st.text_input("Miasto", "Warszawa")
    
    if st.button("Sprawdź pogodę"):
        api_key = "TWOJ_KLUCZ_API"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Temperatura", f"{temp}°C")
            with col2:
                st.write(f"Opis: {desc}")
        else:
            st.error("Nie udało się pobrać danych")
```

---

### 💾 Zapisywanie i wczytywanie danych

#### 1. **JSON**
```python
import json

# Zapisywanie
def save_data():
    with open('data.json', 'w') as f:
        json.dump(st.session_state.todos, f)

# Wczytywanie
def load_data():
    try:
        with open('data.json', 'r') as f:
            st.session_state.todos = json.load(f)
    except FileNotFoundError:
        st.session_state.todos = []
```

#### 2. **CSV**
```python
# Eksport do CSV
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(data)
st.download_button(
    label="📥 Pobierz CSV",
    data=csv,
    file_name='dane.csv',
    mime='text/csv'
)
```

---

## Najlepsze praktyki

### ✅ Do zrobienia

1. **Używaj `session_state` dla stanów**
   ```python
   if 'counter' not in st.session_state:
       st.session_state.counter = 0
   ```

2. **Cachuj kosztowne operacje**
   ```python
   @st.cache_data
   def expensive_computation():
       # ...
   ```

3. **Organizuj kod w funkcje**
   ```python
   def section_name():
       st.header("Tytuł")
       # logika sekcji
   ```

4. **Waliduj dane wejściowe**
   ```python
   if num2 != 0:
       result = num1 / num2
   else:
       st.error("Nie można dzielić przez zero!")
   ```

5. **Używaj `st.columns()` dla layoutu**
   ```python
   col1, col2 = st.columns(2)
   ```

### ❌ Czego unikać

1. **Nie umieszczaj `st.set_page_config()` w środku kodu**
   - Musi być na początku!

2. **Nie używaj zmiennych globalnych bez `session_state`**
   ```python
   # ❌ ŹLE
   counter = 0
   if st.button("+"): counter += 1  # Nie zadziała!
   
   # ✅ DOBRZE
   if 'counter' not in st.session_state:
       st.session_state.counter = 0
   if st.button("+"): st.session_state.counter += 1
   ```

3. **Nie wykonuj ciężkich operacji bez cachowania**
   ```python
   # ❌ ŹLE - wczyta plik przy każdej interakcji
   data = pd.read_csv("huge_file.csv")
   
   # ✅ DOBRZE
   @st.cache_data
   def load_data():
       return pd.read_csv("huge_file.csv")
   ```

4. **Nie twórz nieskończonych pętli z `st.rerun()`**
   ```python
   # ❌ ŹLE
   while True:
       st.rerun()  # Zawiesi aplikację!
   ```

---

## Deployment (wdrożenie)

### Streamlit Cloud (za darmo!)

1. Wypchnij kod na GitHub
2. Wejdź na [share.streamlit.io](https://share.streamlit.io)
3. Połącz z repo GitHub
4. Kliknij "Deploy"

### Wymagania
Stwórz plik `requirements.txt`:
```
streamlit
pandas
numpy
```

---

## Podsumowanie

### Kluczowe koncepty:
- 🔄 **Reactive model** - aplikacja uruchamia się od nowa przy każdej interakcji
- 💾 **Session State** - zachowywanie danych między uruchomieniami
- 📦 **Komponenty** - gotowe elementy UI (przyciski, wykresy, etc.)
- ⚡ **Cachowanie** - optymalizacja wydajności

### Kolejne kroki:
1. Eksperymentuj z różnymi komponentami
2. Dodaj własne sekcje
3. Połącz z API lub bazą danych
4. Wdroż na Streamlit Cloud
5. Podziel się swoim projektem!

### Przydatne zasoby:
- 📖 [Dokumentacja Streamlit](https://docs.streamlit.io)
- 🎨 [Galeria komponentów](https://streamlit.io/components)
- 💡 [Przykłady aplikacji](https://streamlit.io/gallery)
- 🐛 [Forum Streamlit](https://discuss.streamlit.io)

---

**Powodzenia w tworzeniu aplikacji! 🚀**


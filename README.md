# python-projects-portfolio

 Mijn portfolio


# Python Projects Portfolio

This is a collection of simple Python projects I built.

## Projects

### 1. To-do List App
A simple to-do list application for adding, completing, and removing tasks.

### 2. Calculator
A simple calculator that performs addition, subtraction, multiplication, and division.

### 3. Temperature Converter
A program that converts temperatures between Celsius and Fahrenheit.

### 4. Hello, World! (Extended)
An interactive version of the classic "Hello, World!" program.


Mijn bugfixes: 

---

### 1. **To-do lijst applicatie**

#### Basisconcepten:
- **Functies**: De functies `add_task()`, `complete_task()`, en `save_tasks()` laten zien hoe je acties kunt herhalen en organiseren in stukken code.
- **Bestandsbeheer**: De applicatie gebruikt bestanden om taken op te slaan en later te laden met functies als `open()` en `write()`.
- **Lijsten**: Taken worden opgeslagen in een lijst en worden doorlopen met loops.
- **Loops**: Een `while True`-loop wordt gebruikt om de applicatie continu te laten draaien totdat de gebruiker besluit te stoppen.
- **Conditionele statements**: Het programma gebruikt `if-elif-else` om de keuze van de gebruiker af te handelen.

#### bugfixes:
1. **Bestandsfouten**: 
   - Als het tekstbestand voor de taken niet bestaat, kan dit leiden tot een fout. Oplossing: zorg ervoor dat je controleert of het bestand bestaat voordat je het probeert te openen.
   
   **Fix**:
   ```python
   if os.path.exists(filename):
       # open het bestand
   ```

2. **Ongeldige invoer**:
   - Wanneer een gebruiker bijvoorbeeld een letter invoert in plaats van een nummer bij het markeren van een taak als voltooid, kan dit een `ValueError` veroorzaken.

   **Fix**:
   ```python
   try:
       task_no = int(input("Voer het nummer van de taak in: ")) - 1
   except ValueError:
       print("Voer een geldig getal in.")
   ```

3. **Lege invoer voor taken**:
   - Als de gebruiker probeert een lege taak toe te voegen, zou dit vermeden moeten worden.

   **Fix**:
   ```python
   if not task.strip():
       print("Lege taak kan niet worden toegevoegd.")
   ```

---

### 2. **Rekenmachine**

#### Basisconcepten:
- **Functies**: Het gebruik van functies zoals `add()`, `subtract()`, `multiply()`, en `divide()` toont het belang van het opdelen van taken in herbruikbare stukken code.
- **Input en output**: Het programma vraagt om invoer van de gebruiker en geeft resultaten weer met de `input()` en `print()` functies.
- **Conditionele statements**: `if-elif-else` wordt gebruikt om te bepalen welke wiskundige operatie wordt uitgevoerd op basis van de keuze van de gebruiker.
- **Error handling (foutafhandeling)**: Het programma gebruikt een `try-except`-blok om te controleren of de gebruiker een geldig getal invoert.

#### bugfixes:
1. **Delen door nul**:
   - Wanneer de gebruiker een deling uitvoert waarbij de deler nul is, leidt dit tot een `ZeroDivisionError`.

   **Fix**:
   ```python
   if y == 0:
       return "Error: Kan niet delen door 0!"
   ```

2. **Ongeldige invoer (ValueError)**:
   - Wanneer de gebruiker een letter invoert in plaats van een getal, kan dit resulteren in een fout.

   **Fix**:
   ```python
   try:
       num1 = float(input("Voer een getal in: "))
   except ValueError:
       print("Ongeldige invoer. Voer een geldig getal in.")
   ```

3. **Ongeldige keuze in het menu**:
   - Als de gebruiker iets anders invoert dan de opties (1-4), gebeurt er niets of verschijnt er een fout.

   **Fix**:
   ```python
   if keuze not in ["1", "2", "3", "4"]:
       print("Ongeldige keuze.")
   ```

---

### 3. **Temperatuurconversie**

#### Basisconcepten:
- **Functies**: Er zijn twee functies die temperatuurconversies uitvoeren: `celsius_to_fahrenheit()` en `fahrenheit_to_celsius()`. Dit laat zien hoe je dezelfde soort berekeningen in verschillende contexten kunt toepassen.
- **Input en output**: Het programma vraagt de gebruiker om een temperatuur en toont de geconverteerde waarde.
- **Foutafhandeling**: Het programma gebruikt `try-except` om te voorkomen dat de gebruiker niet-numerieke waarden invoert.
- **Conditionele statements**: `if-elif-else` wordt gebruikt om te controleren of de gebruiker een geldige keuze maakt tussen Celsius en Fahrenheit.

#### bugfixes:
1. **Ongeldige invoer (ValueError)**:
   - Wanneer de gebruiker iets invoert dat geen getal is, leidt dit tot een fout.

   **Fix**:
   ```python
   try:
       temp = float(input("Voer de temperatuur in: "))
   except ValueError:
       print("Ongeldige invoer. Voer een geldig getal in.")
   ```

2. **Ongeldige keuze**:
   - Als de gebruiker een andere optie dan 1 of 2 invoert, moet het programma dat opvangen en de gebruiker opnieuw laten kiezen.

   **Fix**:
   ```python
   if keuze not in ["1", "2"]:
       print("Ongeldige keuze.")
   ```

3. **Geen afronding van resultaten**:
   - Soms worden er te veel decimalen weergegeven, wat onoverzichtelijk is.

   **Fix**:
   ```python
   print(f"{celsius:.2f}°C is gelijk aan {fahrenheit:.2f}°F")
   ```

---

### 4. **Hello, World! (uitgebreid)**

#### Basisconcepten:
- **Functies**: De functie `greet_user()` wordt gebruikt om een persoonlijke begroeting te tonen. Dit illustreert hoe functies parameters kunnen accepteren en verwerken.
- **Input**: Het programma vraagt de gebruiker om een naam in te voeren en gebruikt die in een aangepaste begroeting.
- **Output**: Het programma toont de "Hello, World!"-boodschap en een persoonlijke begroeting met de ingevoerde naam.
- **F-strings**: Dit laat zien hoe f-strings werken om variabelen in een string te interpoleren, een veelgebruikte manier om gegevens in een string te plaatsen.

#### bugfixes:
1. **Fout bij f-strings in oudere Python-versies**:
   - Als je een versie van Python ouder dan 3.6 gebruikt, werken f-strings niet.

   **Fix**: Gebruik ouderwetse string formatting voor oudere versies van Python:
   ```python
   print("Hello, {}! Welcome to Python.".format(name))
   ```

2. **Vergeten om de functie aan te roepen**:
   - Beginners vergeten soms de functie `greet_user()` in de `main()`-functie aan te roepen, waardoor de begroeting niet wordt weergegeven.

   **Fix**:
   ```python
   greet_user(user_name)
   ```

3. **Lege invoer voor naam**:
   - Als de gebruiker geen naam invoert, kan het programma onverwacht gedrag vertonen.

   **Fix**:
   ```python
   if not user_name.strip():
       print("Geen naam ingevoerd. Probeer opnieuw.")
   ```



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


Hier zijn voor elk van de vier projecten veelvoorkomende fouten die beginnende programmeurs maken, samen met oplossingen:

---

### 1. **To-do lijst applicatie**

#### Veelvoorkomende fouten:
- **Bestandsfouten (FileNotFoundError)**: Als het tekstbestand voor de taken niet bestaat, kan dit een fout veroorzaken wanneer je probeert taken te laden.
  - **Oplossing**: Controleer of het bestand bestaat en maak een leeg bestand aan als dat niet het geval is:
    ```python
    if not os.path.exists(filename):
        with open(filename, 'w'): pass
    ```

- **Ongeldige invoer (ValueError)**: Wanneer een gebruiker bijvoorbeeld letters invoert in plaats van een nummer bij het voltooien van een taak, kan dit een `ValueError` veroorzaken.
  - **Oplossing**: Gebruik foutafhandeling om dergelijke fouten op te vangen:
    ```python
    try:
        task_no = int(input("Voer een geldig nummer in: ")) - 1
    except ValueError:
        print("Voer een getal in.")
    ```

- **Lege invoer**: Als een gebruiker probeert een lege taak toe te voegen, wordt deze nog steeds opgeslagen.
  - **Oplossing**: Voeg een controle toe om ervoor te zorgen dat lege invoer niet wordt toegevoegd:
    ```python
    if not task.strip():
        print("Lege taak kan niet worden toegevoegd.")
    ```

---

### 2. **Rekenmachine**

#### Veelvoorkomende fouten:
- **Delen door nul (ZeroDivisionError)**: Wanneer de gebruiker een deling uitvoert met 0, resulteert dit in een fout.
  - **Oplossing**: Voeg een controle toe in de `divide()`-functie om dit te voorkomen:
    ```python
    if y == 0:
        return "Error: Kan niet delen door 0!"
    ```

- **Ongeldige invoer (ValueError)**: Wanneer de gebruiker letters invoert in plaats van getallen, kan dit leiden tot invoerfouten.
  - **Oplossing**: Gebruik `try-except` om foutieve invoer te verwerken:
    ```python
    try:
        num1 = float(input("Voer een getal in: "))
    except ValueError:
        print("Voer een geldig getal in.")
    ```

- **Ongeldige keuze in het menu**: Als de gebruiker iets anders dan 1-4 invoert, doet de calculator niets of geeft een fout.
  - **Oplossing**: Voeg een controle toe voor ongeldige menu-invoer:
    ```python
    if choice not in ["1", "2", "3", "4"]:
        print("Ongeldige keuze. Probeer opnieuw.")
    ```

---

### 3. **Temperatuurconversie**

#### Veelvoorkomende fouten:
- **Ongeldige invoer (ValueError)**: Wanneer de gebruiker een niet-numerieke waarde invoert voor de temperatuur, resulteert dit in een fout.
  - **Oplossing**: Gebruik `try-except` om foutieve invoer af te handelen:
    ```python
    try:
        celsius = float(input("Voer een getal in: "))
    except ValueError:
        print("Ongeldige invoer. Voer een geldig getal in.")
    ```

- **Ongeldige keuze in het menu**: Wanneer de gebruiker een andere waarde dan 1 of 2 invoert, kan het programma foutief werken.
  - **Oplossing**: Voeg een controle toe voor geldige keuzes:
    ```python
    if keuze not in ["1", "2"]:
        print("Ongeldige keuze.")
    ```

- **Geen afronding van resultaten**: De resultaten kunnen te veel decimalen hebben, wat het resultaat onoverzichtelijk maakt.
  - **Oplossing**: Gebruik formatteertekens om de output te beperken tot bijvoorbeeld twee decimalen:
    ```python
    print(f"{celsius:.2f}°C is gelijk aan {fahrenheit:.2f}°F")
    ```

---

### 4. **Hello, World! (uitgebreid)**

#### Veelvoorkomende fouten:
- **Fout bij f-strings in oudere Python-versies**: Als je Python 3.5 of lager gebruikt, krijg je een fout met f-strings.
  - **Oplossing**: Zorg ervoor dat je Python 3.6 of hoger gebruikt, of gebruik ouderwetse string formatting:
    ```python
    print("Hello, {}! Welcome to Python.".format(name))
    ```

- **Vergeten om een functie aan te roepen**: Beginners vergeten soms om de functie aan te roepen in de `main()`-functie, waardoor het programma niets doet.
  - **Oplossing**: Controleer of de functie `greet_user(user_name)` correct wordt aangeroepen binnen `main()`.

- **Geen foutafhandeling voor invoer**: Wanneer de gebruiker niets invoert, kan het programma onverwacht gedrag vertonen.
  - **Oplossing**: Voeg een eenvoudige controle toe om te zien of de invoer leeg is:
    ```python
    if not user_name.strip():
        print("Geen naam ingevoerd. Probeer opnieuw.")
    ```

---

### Algemene tips voor beginners:
1. **Leesbare foutmeldingen**: Begrijp de foutmeldingen die Python geeft en gebruik deze om je code te debuggen. Elke fout heeft een regelnummer en een korte uitleg.
   
2. **Veel testen**: Test je programma regelmatig door verschillende soorten invoer te proberen. Test bijvoorbeeld zowel geldige als ongeldige invoer.

3. **Kleine stappen**: Probeer je programma in kleine stappen te bouwen. Voeg steeds kleine stukjes functionaliteit toe en test ze grondig voordat je verder gaat.

4. **Documentatie en commentaar**: Voeg commentaar toe in je code om uit te leggen wat elke functie doet. Dit helpt je om de logica van je programma te begrijpen wanneer je eraan werkt.

Met deze richtlijnen en foutoplossingen kun je typische beginnersfouten voorkomen en jezelf helpen beter te programmeren.

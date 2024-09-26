## 1. **To-do Lijst Applicatie**

### Beschrijving:
Een eenvoudige to-do lijst applicatie waarin de gebruiker taken kan toevoegen, voltooien, en verwijderen. De taken worden opgeslagen in een tekstbestand, zodat de lijst behouden blijft na het sluiten van de applicatie.

### Gebruikte technieken:
- **Bestandsbeheer**: Taken worden opgeslagen in een tekstbestand (`todo_list.txt`), wat laat zien hoe je bestanden kunt openen, lezen, schrijven en manipuleren in Python.
- **Functies**: Verschillende functies worden gebruikt om de code georganiseerd en herbruikbaar te maken (bijv. voor het toevoegen, voltooien en weergeven van taken).
- **Loops**: De applicatie blijft herhalen totdat de gebruiker ervoor kiest om af te sluiten.
- **Input/Output**: De gebruiker kan input geven (bijvoorbeeld het toevoegen van een taak), en de output wordt weergegeven in de console.

### Basisprincipes:
- **Bestandsbeheer in Python**: In dit project wordt de `open()`-functie gebruikt om taken op te slaan en op te halen van een tekstbestand. Het begrijpen van hoe je bestanden beheert, is essentieel voor veel toepassingen in softwareontwikkeling.
  - Voorbeeld:
    ```python
    with open("todo_list.txt", "w") as f:
        f.write("Nieuwe taak")
    ```

- **Functies en modulariteit**: Functies maken je code herbruikbaar en overzichtelijk. In dit project worden de taken zoals toevoegen, verwijderen en voltooien van taken in afzonderlijke functies georganiseerd.

### Bugfixes:
- **Bestand niet gevonden**: Als het bestand `todo_list.txt` niet bestaat, kan de applicatie falen. Oplossing: controleer of het bestand bestaat, en maak het indien nodig aan.
- **Foute invoer**: Wanneer de gebruiker een letter invoert in plaats van een cijfer om een taak te voltooien. Oplossing: Gebruik foutafhandeling (`try-except`) om niet-numerieke invoer af te vangen.

---

## 2. **Rekenmachine**

### Beschrijving:
Een eenvoudige calculator die de vier basisbewerkingen uitvoert: optellen, aftrekken, vermenigvuldigen en delen.

### Gebruikte technieken:
- **Functies**: Voor elke bewerking (optellen, aftrekken, vermenigvuldigen, delen) wordt een afzonderlijke functie gebruikt om de structuur van de code overzichtelijk te houden.
- **Conditionele statements**: Er wordt gebruik gemaakt van `if-else` om de invoer van de gebruiker te interpreteren en de juiste functie op te roepen.
- **Input/Output**: De gebruiker kan twee getallen invoeren en een bewerking kiezen.

### Basisprincipes:
- **Functies**: In dit project wordt aangetoond hoe functies worden gebruikt om herhaling te voorkomen. Elke bewerking (zoals optellen of aftrekken) is geïsoleerd in een aparte functie, wat helpt om de logica schoon en herbruikbaar te houden.
  - Voorbeeld:
    ```python
    def add(x, y):
        return x + y
    ```

- **Conditionele logica**: De keuze van de gebruiker wordt gebruikt om te bepalen welke bewerking wordt uitgevoerd, wat aantoont hoe je `if-else`-constructies kunt gebruiken om beslissingen te nemen in de code.
  - Voorbeeld:
    ```python
    if choice == "1":
        print(add(num1, num2))
    ```

### Bugfixes:
- **Delen door nul**: Wanneer de gebruiker probeert te delen door nul, zal de applicatie een fout veroorzaken. Oplossing: Voeg een controle toe om deling door nul te voorkomen.
- **Foute invoer**: Letters of andere niet-numerieke invoer kunnen fouten veroorzaken. Oplossing: Gebruik foutafhandeling om te zorgen dat de invoer geldig is.

---

## 3. **Temperatuurconversie**

### Beschrijving:
Een programma dat temperaturen converteert tussen Celsius en Fahrenheit. De gebruiker kan kiezen welke conversie hij/zij wil uitvoeren.

### Gebruikte technieken:
- **Functies**: Er worden functies gebruikt om de conversies uit te voeren (Celsius naar Fahrenheit en andersom).
- **Input/Output**: De gebruiker voert een temperatuur in en krijgt de geconverteerde waarde terug.
- **Conditionele statements**: Het programma controleert de invoer van de gebruiker om te bepalen welke conversie moet worden uitgevoerd.

### Basisprincipes:
- **Mathematische bewerkingen**: Dit project introduceert basale wiskundige berekeningen in Python. Formules zoals de conversie van Celsius naar Fahrenheit worden geïmplementeerd in functies.
  - Voorbeeld:
    ```python
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    ```

- **Functies en return-waarden**: Dit project toont aan hoe functies parameters kunnen ontvangen en een waarde kunnen teruggeven, wat een fundamenteel concept in programmeren is.

### Bugfixes:
- **Foute invoer**: Als de gebruiker iets anders dan een getal invoert, zal het programma falen. Oplossing: Voeg foutafhandeling toe om te zorgen dat de invoer geldig is.
- **Onjuist menu-keuze**: Als de gebruiker een keuze maakt die niet in het menu staat, kan het programma niet reageren. Oplossing: Voeg een controle toe voor geldige keuzes.

---

## 4. **Hello, World! (Uitgebreid)**

### Beschrijving:
Een eenvoudige versie van "Hello, World!" waarin de gebruiker interactief wordt begroet op basis van hun naam.

### Gebruikte technieken:
- **Input/Output**: De gebruiker voert hun naam in, en het programma begroet hen op basis van deze invoer.
- **Functies**: Er wordt een functie gebruikt om de begroeting aan te maken.
- **String-interpolatie**: De invoer van de gebruiker wordt in de begroeting geïntegreerd door gebruik te maken van f-strings.

### Basisprincipes:
- **Functies**: Dit project toont een eenvoudige implementatie van functies waarin de invoer van de gebruiker wordt verwerkt en een bericht wordt teruggegeven.
  - Voorbeeld:
    ```python
    def greet_user(name):
        print(f"Hello, {name}! Welcome to Python.")
    ```

- **String-interpolatie (f-strings)**: In dit project wordt een f-string gebruikt om de naam van de gebruiker in een bericht te verwerken. Dit is een handige manier om variabelen in strings te verwerken.
  - Voorbeeld:
    ```python
    print(f"Hello, {name}!")
    ```

### Bugfixes:
- **Vergeten om een functie aan te roepen**: Beginners vergeten soms om de functie aan te roepen, waardoor de begroeting niet verschijnt. Oplossing: Zorg ervoor dat je functie wordt aangeroepen in de `main()`-functie.
- **Lege invoer**: Als de gebruiker niets invoert voor hun naam, kan dit onverwacht gedrag veroorzaken. Oplossing: Voeg een controle toe om te zorgen dat de invoer niet leeg is.

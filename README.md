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












### Algemene tips voor het gesprek:
- **Wees zelfverzekerd**: Je hebt deze projecten zelf gebouwd en elk project toont verschillende belangrijke vaardigheden. Wees trots op wat je hebt bereikt.
- **Wees eerlijk**: Als je iets niet weet of nog aan het leren bent, is dat prima! Een goede coach waardeert je openheid en leergierigheid.
- **Blijf kalm en voorbereid**: Deze cheatsheet helpt je om eventuele vragen over je werk te beantwoorden. Neem de tijd om rustig uit te leggen wat je hebt gedaan.

---

### Project 1: **To-do Lijst Applicatie**

- **Wat het project doet**:
  - Dit is een eenvoudige applicatie waarmee de gebruiker taken kan toevoegen, voltooien, en verwijderen.
  - De taken worden opgeslagen in een tekstbestand, zodat de gebruiker de lijst later kan openen.

- **Waarom dit project belangrijk is**:
  - Het toont dat je **bestandsbeheer** begrijpt en hoe je data persistent maakt (opgeslagen na afsluiten).
  - Het laat zien dat je weet hoe je **functies** kunt gebruiken om je code georganiseerd te houden.
  - Het is een voorbeeld van een eenvoudige maar nuttige applicatie die veel gebruikers dagelijks gebruiken.

- **Veelvoorkomende fout**:
  - Als de gebruiker een fout maakt bij het invoeren van een taaknummer, kan de applicatie crashen. Dit project laat zien dat je hebt nagedacht over **foutafhandeling**.

- **Kritische vraag om voor te bereiden**:
  - **Waarom heb je gekozen om de data in een tekstbestand op te slaan en niet bijvoorbeeld in een database?**
    - Antwoord: Voor een eenvoudige applicatie zoals deze is een tekstbestand efficiënt en makkelijk. Een database zou overkill zijn voor deze schaal, maar ik zou in een toekomstige versie een database kunnen implementeren om de applicatie robuuster te maken.

---

### Project 2: **Rekenmachine**

- **Wat het project doet**:
  - Een eenvoudige calculator die basisbewerkingen zoals optellen, aftrekken, vermenigvuldigen en delen uitvoert.
  
- **Waarom dit project belangrijk is**:
  - Het toont je begrip van **functies** en hoe je kleine, herbruikbare stukjes code kunt schrijven voor elke bewerking.
  - Het laat zien dat je gebruik kunt maken van **conditionele logica** (zoals `if-else`) om beslissingen te nemen op basis van gebruikersinvoer.

- **Veelvoorkomende fout**:
  - Delen door nul zou een fout kunnen geven. Dit project laat zien dat je hebt nagedacht over het controleren van randgevallen.

- **Kritische vraag om voor te bereiden**:
  - **Hoe zorg je ervoor dat gebruikers geen ongeldige invoer geven, zoals tekst in plaats van een getal?**
    - Antwoord: Ik heb foutafhandeling toegevoegd met `try-except`, zodat de applicatie een foutmelding geeft in plaats van te crashen wanneer de invoer ongeldig is.

---

### Project 3: **Temperatuurconversie**

- **Wat het project doet**:
  - Het converteert temperaturen tussen Celsius en Fahrenheit, afhankelijk van de keuze van de gebruiker.
  
- **Waarom dit project belangrijk is**:
  - Het project toont je vermogen om **wiskundige berekeningen** te implementeren en uit te voeren in Python.
  - Het laat zien dat je input van de gebruiker kunt verwerken en op basis daarvan de juiste conversie kunt uitvoeren.

- **Veelvoorkomende fout**:
  - Als de gebruiker iets anders dan een getal invoert, kan het programma crashen. Dit project illustreert hoe je **foutafhandeling** implementeert.

- **Kritische vraag om voor te bereiden**:
  - **Waarom is foutafhandeling zo belangrijk in applicaties zoals deze?**
    - Antwoord: Foutafhandeling zorgt ervoor dat de applicatie niet crasht als gebruikers onverwachte invoer geven. Dit maakt de applicatie robuuster en gebruiksvriendelijker.

---

### Project 4: **Hello, World! (Uitgebreid)**

- **Wat het project doet**:
  - Dit is een interactieve versie van het klassieke "Hello, World!" programma. Het begroet de gebruiker met hun naam.
  
- **Waarom dit project belangrijk is**:
  - Het introduceert het gebruik van **input/output** en toont hoe je gebruikersinvoer kunt verwerken.
  - Het project maakt gebruik van **f-strings** in Python om variabelen in een string te integreren, wat een modern en efficiënt gebruik van string-interpolatie laat zien.

- **Veelvoorkomende fout**:
  - Als de gebruiker geen naam invoert, kan het programma onverwachte resultaten geven. Hier is een eenvoudige controle geïmplementeerd om dat te voorkomen.

- **Kritische vraag om voor te bereiden**:
  - **Waarom heb je f-strings gebruikt in plaats van een andere manier om strings te formatteren?**
    - Antwoord: F-strings zijn in Python 3.6 en hoger een efficiëntere en makkelijkere manier om strings te formatteren. Ze zijn sneller dan traditionele methoden zoals `.format()` en maken de code leesbaarder.

---

### Algemene vragen om voor te bereiden:

1. **Waarom heb je deze specifieke projecten gekozen?**
   - Antwoord: Elk project vertegenwoordigt een fundamenteel concept in programmeren, zoals bestandsbeheer, foutafhandeling, conditionele logica, en gebruikersinvoer. Deze projecten laten een breed scala aan vaardigheden zien die relevant zijn voor softwareontwikkeling.

2. **Wat heb je geleerd tijdens het bouwen van deze projecten?**
   - Antwoord: Ik heb geleerd hoe belangrijk het is om gestructureerde en herbruikbare code te schrijven, hoe je foutafhandeling implementeert om de gebruikerservaring te verbeteren, en hoe je gebruikersinvoer verwerkt en daarop reageert.

3. **Hoe zou je deze projecten in de toekomst verbeteren?**
   - Antwoord: Ik zou bijvoorbeeld de to-do lijst kunnen uitbreiden met een database voor betere opslag, en de rekenmachine uitbreiden met complexere functies zoals exponenten of wortels. Verder zou ik meer aandacht kunnen besteden aan het maken van een grafische gebruikersinterface voor sommige projecten.

---

## Project 5: **Bingo Spel Applicatie (GUI)**

### Beschrijving:
Het Bingo Spel is een interactieve GUI-applicatie waarbij de gebruiker bingo-kaarten kan genereren en spelen tegen de computer. Het spel is ontworpen om een klassieke Bingo-ervaring te bieden, waarbij willekeurige nummers worden getrokken en zowel de speler als de computer proberen zo snel mogelijk een volledige rij, kolom of diagonaal te markeren. De applicatie maakt gebruik van de `Tkinter`-bibliotheek voor een visueel aantrekkelijke interface.

### Gebruikte technieken:
- **Grafische Gebruikersinterface (GUI)**: De applicatie is gebouwd met `Tkinter` en maakt gebruik van verschillende GUI-elementen zoals knoppen, labels en frames om een overzichtelijke en interactieve ervaring te bieden.
- **Evenementgestuurde programmering**: Door middel van `event handlers` reageert de applicatie op gebruikersacties, zoals het klikken van knoppen voor het trekken van nummers.
- **Data structureren**: De Bingo-kaarten worden opgeslagen in geneste lijsten en dictionaries, wat een efficiënte manier biedt om nummers te controleren en gemarkeerde vakjes bij te houden.
- **Random getallen**: Willekeurige getallen worden gegenereerd met behulp van de `random`-module om Bingo-kaarten te vullen en nummers te trekken, wat zorgt voor een unieke speelervaring bij elke sessie.

### Basisprincipes:
- **Evenementgestuurde programmering**: In een GUI-applicatie is het belangrijk dat de logica op de juiste manier reageert op gebruikersacties. Door `event handlers` te koppelen aan knoppen en andere GUI-elementen, wordt de applicatie dynamischer en gebruikersvriendelijker.
- **Complexe datastructuren**: Lijsten en dictionaries worden gebruikt om de Bingo-kaarten te beheren, waardoor het gemakkelijk is om rijen, kolommen en diagonalen te controleren op een volledige Bingo.
- **Synchronisatie tussen GUI en logica**: De GUI moet te allen tijde de actuele status van het spel weergeven. Met `root.update()` wordt de interface gesynchroniseerd met de logica, zodat de gebruiker direct feedback krijgt bij elke actie.

### Bugfixes:
- **Dubbele nummers op kaarten**: Bij het genereren van Bingo-kaarten kunnen er soms dubbele nummers ontstaan. Oplossing: Een set wordt gebruikt om ervoor te zorgen dat elk nummer uniek is in een kolom.
- **GUI loopt vast**: Bij het trekken van nummers kan de GUI vastlopen als de update-logica inefficiënt is. Oplossing: Gebruik `root.update()` en optimaliseer de logica om de verwerkingsbelasting te minimaliseren.
- **Verkeerde invoer in de GUI**: Als de gebruiker een ongeldige actie probeert uit te voeren, kan dit leiden tot een vastloper of onverwacht gedrag. Oplossing: Voeg foutafhandeling toe in de event handlers en geef meldingen in de GUI.

### Kritische vragen om voor te bereiden:
1. **Waarom heb je gekozen voor `Tkinter` in plaats van een andere GUI-bibliotheek zoals `PyQt`?**  
   `Tkinter` is een ingebouwde bibliotheek in Python en biedt een eenvoudig instappunt voor het maken van GUI-applicaties. Voor een project van deze schaal biedt `Tkinter` alle benodigde functionaliteit zonder extra dependencies.
2. **Hoe controleer je of een speler of de computer Bingo heeft?**  
   Elke rij, kolom en diagonaal op de Bingo-kaart wordt gecontroleerd op gemarkeerde nummers. Als een van deze patronen volledig gemarkeerd is, heeft de speler of de computer Bingo.
3. **Hoe zorg je ervoor dat de GUI altijd synchroon is met de spelstatus?**  
   De GUI wordt continu geüpdatet met behulp van de `config()`-methode van `Tkinter`, waarmee labels en andere interface-elementen worden aangepast op basis van de actuele status van het spel.

### Verbeteringen voor de toekomst:
- **Meerdere winpatronen**: Naast horizontale, verticale en diagonale lijnen kunnen extra winpatronen zoals hoeken of een vol blok worden toegevoegd.
- **Multiplayer-mogelijkheid**: De applicatie zou kunnen worden uitgebreid met een optie voor meerdere spelers, waarbij elke speler een eigen kaart heeft.
- **Online-functionaliteit**: De huidige versie is lokaal. Een toekomstige versie zou kunnen worden uitgebreid met netwerkfunctionaliteit zodat spelers online tegen elkaar kunnen spelen.

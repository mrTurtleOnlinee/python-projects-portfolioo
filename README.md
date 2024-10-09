## 1. **To-do Lijst Applicatie**

### Beschrijving:
Een eenvoudige to-do lijst applicatie waarin de gebruiker taken kan toevoegen, voltooien en verwijderen. De taken worden opgeslagen in een tekstbestand (`todo_list.txt`), zodat de lijst behouden blijft na het sluiten van de applicatie.

### Gebruikte technieken:
- **Bestandsbeheer**: Taken worden opgeslagen in een tekstbestand. Dit laat zien hoe je bestanden kunt openen, lezen en schrijven in Python.
- **Functies**: Functies worden gebruikt om de code georganiseerd en herbruikbaar te maken (bijv. voor het toevoegen, voltooien en weergeven van taken).
- **Input/Output en Loops**: De applicatie verwerkt invoer van de gebruiker en herhaalt het proces totdat de gebruiker kiest om af te sluiten.

### Basisprincipes:
- **Bestandsbeheer**: Het gebruik van de `open()`-functie om taken op te slaan en op te halen uit een tekstbestand is een essentiële vaardigheid in softwareontwikkeling.
- **Functies en modulariteit**: Door verschillende taken op te splitsen in functies, blijft de code schoon en overzichtelijk.

### Bugfixes:
- **Bestand niet gevonden**: Als `todo_list.txt` niet bestaat, creëert de applicatie het bestand automatisch.
- **Foute invoer**: Foutafhandeling (`try-except`) wordt gebruikt om niet-numerieke invoer op te vangen.

---

## 2. **Rekenmachine**

### Beschrijving:
Een calculator die de vier basisbewerkingen uitvoert: optellen, aftrekken, vermenigvuldigen en delen.

### Gebruikte technieken:
- **Functies**: Voor elke bewerking (optellen, aftrekken, vermenigvuldigen, delen) is er een aparte functie om de structuur van de code overzichtelijk te houden.
- **Conditionele statements**: `if-else` wordt gebruikt om de gebruikerskeuze te interpreteren en de juiste bewerking uit te voeren.

### Basisprincipes:
- **Functies en conditionele logica**: Functies helpen bij het organiseren van de logica en herbruikbaarheid van code. `if-else`-constructies helpen bij het nemen van beslissingen op basis van gebruikersinvoer.

### Bugfixes:
- **Delen door nul**: Er is een controle toegevoegd om deling door nul te voorkomen.
- **Foute invoer**: Foutafhandeling wordt gebruikt om niet-numerieke invoer op te vangen.

---

## 3. **Temperatuurconversie**

### Beschrijving:
Een programma dat temperaturen converteert tussen Celsius en Fahrenheit, afhankelijk van de keuze van de gebruiker.

### Gebruikte technieken:
- **Functies**: Functies worden gebruikt om de conversies uit te voeren.
- **Input/Output en conditionele statements**: Het programma controleert de invoer en bepaalt welke conversie moet worden uitgevoerd.

### Basisprincipes:
- **Wiskundige berekeningen**: Formules voor de conversie van Celsius naar Fahrenheit en omgekeerd worden geïmplementeerd in functies.
- **Functies en return-waarden**: Dit project toont aan hoe functies parameters kunnen ontvangen en een waarde kunnen teruggeven.

### Bugfixes:
- **Foute invoer**: Er is foutafhandeling toegevoegd om niet-numerieke invoer op te vangen.

---

## 4. **Hello, World! (Uitgebreid)**

### Beschrijving:
Een interactieve versie van "Hello, World!" waarbij de gebruiker wordt begroet op basis van hun naam.

### Gebruikte technieken:
- **Input/Output**: De gebruiker voert hun naam in, en het programma geeft een gepersonaliseerde begroeting.
- **Functies en string-interpolatie**: F-strings worden gebruikt om de naam van de gebruiker in de begroeting op te nemen.

### Basisprincipes:
- **Functies en string-interpolatie**: Door gebruik te maken van f-strings kunnen variabelen eenvoudig in strings worden verwerkt.

### Bugfixes:
- **Lege invoer**: Er is een controle toegevoegd om te zorgen dat de invoer niet leeg is.

---

## 5. **Bingo Spel Applicatie (GUI)**

### Beschrijving:
Het Bingo Spel is een interactieve GUI-applicatie waarbij de gebruiker bingo-kaarten kan genereren en spelen tegen de computer. Het spel is ontworpen om een klassieke Bingo-ervaring te bieden, waarbij willekeurige nummers worden getrokken en zowel de speler als de computer proberen zo snel mogelijk een volledige rij, kolom of diagonaal te markeren. De applicatie maakt gebruik van de `Tkinter`-bibliotheek voor een visueel aantrekkelijke interface.

### Gebruikte technieken:
- **Grafische Gebruikersinterface (GUI)**: De applicatie is gebouwd met `Tkinter` en maakt gebruik van verschillende GUI-elementen zoals knoppen, labels en frames om een overzichtelijke en interactieve ervaring te bieden.
- **Evenementgestuurde programmering**: De applicatie reageert op gebruikersacties zoals het klikken van knoppen voor het trekken van nummers.
- **Data structureren**: De Bingo-kaarten worden opgeslagen in geneste lijsten en dictionaries.
- **Willekeurige getallen**: De `random`-module wordt gebruikt om Bingo-kaarten te vullen en nummers te trekken.

### Basisprincipes:
- **Evenementgestuurde programmering**: De logica reageert op gebruikersacties via event handlers.
- **Complexe datastructuren**: Lijsten en dictionaries worden gebruikt om de Bingo-kaarten te beheren.
- **Synchronisatie tussen GUI en logica**: De GUI moet altijd de actuele status van het spel weergeven.

### Bugfixes:
- **Dubbele nummers**: Gebruik van sets om dubbele nummers op kaarten te vermijden.
- **GUI-reactietijd**: Optimalisaties om vastlopers bij het trekken van nummers te voorkomen.
- **Verkeerde invoer**: Foutafhandeling in de GUI voor ongeldig gebruik.

### Verbeteringen voor de toekomst:
- **Multiplayer-mogelijkheid en online-functionaliteit**: Toevoegen van meerdere spelers en de mogelijkheid om online te spelen.

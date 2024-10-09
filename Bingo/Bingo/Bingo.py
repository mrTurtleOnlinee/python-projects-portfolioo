import random  # Dit stelt ons in staat om willekeurige keuzes en getallen te maken.
import os      # Hiermee kunnen we systeemgerelateerde functies gebruiken, zoals het legen van het scherm.

# Deze functie maakt het scherm schoon, net zoals je een nieuw wit blad krijgt.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # Leegt het scherm, afhankelijk van je besturingssysteem.
    print("\033[H\033[J", end="")  # Zet de cursor naar de bovenkant van het scherm, zodat het lijkt alsof het scherm schoon is.

# Deze functie maakt een nieuwe bingokaart.
def create_bingo_card():
    bingo_card = {}  # Maak een lege bingokaart (zoals een leeg vel papier).
    columns = ["B", "I", "N", "G", "O"]  # Elke kolom van de bingokaart heeft een letter.
    for i, column in enumerate(columns):  # Voor elke kolom...
        # Kies 5 willekeurige getallen binnen een bepaalde range (1-15 voor B, 16-30 voor I, etc.).
        bingo_card[column] = random.sample(range(i * 15 + 1, i * 15 + 16), 5)
    bingo_card["N"][2] = "Free"  # Het middelste vakje is altijd gratis.
    return bingo_card  # Geef de voltooide bingokaart terug.

# Deze functie toont de bingokaart met een mooie ASCII-omlijning (zoals een kader).
def print_bingo_card(bingo_card, marked):
    print("+" + "-" * 29 + "+")  # Teken de bovenrand.
    print("|  B    |   I    |   N    |   G    |   O   |")  # Print de koptekst van de kaart.
    print("+" + "-" * 29 + "+")  # Teken een scheidingslijn.

    # Voor elke rij in de kaart...
    for row in range(5):
        print("|", end=" ")  # Start de rij met een lijntje.
        for column in ["B", "I", "N", "G", "O"]:
            # Als een getal gemarkeerd is (aangevinkt), omring het met sterretjes, anders toon het normaal.
            cell = str(bingo_card[column][row]).center(5)
            if marked[column][row]:  # Check of dit getal al gemarkeerd is.
                cell = f"*{cell.strip()}*".center(5)
            print(cell, end=" | ")  # Print de cel van de kaart.
        print()  # Ga naar de volgende rij.
    print("+" + "-" * 29 + "+")  # Teken de onderrand van de kaart.

# Deze functie print een koptekst voor het spel, zodat het er mooi uitziet.
def print_header():
    print("\n" + "=" * 80)  # Teken een dikke lijn bovenaan.
    print(" " * 35 + "BINGO SPEL")  # Zet de titel "BINGO SPEL" in het midden.
    print("=" * 80 + "\n")  # Teken een dikke lijn onderaan.

# Deze functie laat de hele lay-out zien, inclusief de bingokaart van de speler en het laatst geroepen nummer.
def print_layout(player_card, marked, current_number=None):
    clear_screen()  # Maak het scherm schoon voordat we de nieuwe layout tekenen.
    print_header()  # Print de titel van het spel.
    if current_number:  # Als er een nummer is geroepen, laat het zien.
        print(f"Nummer {current_number} is geroepen.\n")
    print("Jouw Bingokaart:")  # Laat de speler weten dat dit hun kaart is.
    print_bingo_card(player_card, marked)  # Toon de bingokaart van de speler.
    print("\n" + "-" * 80 + "\n")  # Teken een scheidingslijn.
    print("\n" + "Druk op Enter om door te gaan...".center(80))  # Vraag de speler om op Enter te drukken om door te gaan.
    print("\n" + "-" * 80)  # Teken nog een scheidingslijn.

# Deze functie controleert of er Bingo is door te kijken naar rijen, kolommen of diagonalen.
def check_bingo(bingo_card, marked):
    # Controleer elke rij of alle getallen gemarkeerd zijn.
    rows = [all(marked[column][row] for column in ["B", "I", "N", "G", "O"]) for row in range(5)]
    # Controleer elke kolom of alle getallen gemarkeerd zijn.
    columns = [all(marked[column][row] for row in range(5)) for column in ["B", "I", "N", "G", "O"]]
    # Controleer de twee diagonalen (schuin over de kaart).
    diagonal1 = all(marked[column][i] for i, column in enumerate(["B", "I", "N", "G", "O"]))
    diagonal2 = all(marked[column][4 - i] for i, column in enumerate(["B", "I", "N", "G", "O"]))
    
    # Als er één rij, kolom of diagonaal gemarkeerd is, is er Bingo!
    return any(rows) or any(columns) or diagonal1 or diagonal2

# Deze functie maakt een aantal willekeurige spelers (bots) aan die ook meedoen aan het spel.
def create_random_players(num_players):
    players = []  # Maak een lege lijst voor de spelers.
    for _ in range(num_players):
        card = create_bingo_card()  # Geef elke speler een eigen bingokaart.
        marked = {column: [False] * 5 for column in ["B", "I", "N", "G", "O"]}  # Niets is gemarkeerd aan het begin.
        players.append({'card': card, 'marked': marked})  # Voeg de speler toe aan de lijst.
    return players  # Geef de lijst van spelers terug.

# Deze functie markeert het geroepen nummer op de kaarten van de bots.
def update_random_players(players, number):
    for player in players:  # Voor elke speler...
        card = player['card']
        marked = player['marked']
        for column in card:  # Check elke kolom op het nummer.
            if number in card[column]:  # Als het nummer op de kaart staat...
                index = card[column].index(number)  # Zoek de positie van het nummer.
                marked[column][index] = True  # Markeer het als aangevinkt.

# Deze functie kijkt of een van de bots Bingo heeft.
def any_random_player_has_bingo(players):
    for player in players:  # Voor elke bot...
        if check_bingo(player['card'], player['marked']):  # Check of ze Bingo hebben.
            return True  # Als er een bot Bingo heeft, eindigt het spel.
    return False  # Als geen enkele bot Bingo heeft, gaat het spel verder.

# Dit is de hoofdfunctie die het hele spel start en beheert.
def play_bingo():
    # Maak de kaart voor de speler aan.
    player_card = create_bingo_card()
    player_marked = {column: [False] * 5 for column in ["B", "I", "N", "G", "O"]}  # De speler heeft nog niets gemarkeerd.

    # Maak willekeurige bots aan die ook meedoen.
    random_players = create_random_players(random.randint(10, 35))  # Kies een willekeurig aantal bots tussen 10 en 35.
    print(f"Het spel begint met {len(random_players)} willekeurige deelnemers naast jou!\n")

    # Maak een lijst van alle mogelijke bingogetallen (1 t/m 75) en schud ze door elkaar.
    all_numbers = list(range(1, 76))
    random.shuffle(all_numbers)

    input("Druk op Enter om het spel te starten...\n")  # Wacht op de speler om het spel te starten.
    print_layout(player_card, player_marked)  # Toon de eerste layout.

    # Dit is de hoofdspel-lus die doorgaat totdat er Bingo is of de getallen op zijn.
    while True:
        if not all_numbers:  # Als er geen getallen meer zijn, eindigt het spel.
            print("Geen nummers meer over! Het spel eindigt.")
            break

        number = all_numbers.pop()  # Roep een nieuw getal (haal het van de stapel).
        
        # Markeer het getal op de kaart van de speler als het aanwezig is.
        for column in player_card:
            if number in player_card[column]:
                index = player_card[column].index(number)
                player_marked[column][index] = True

        # Update de kaarten van de bots met het nieuwe getal.
        update_random_players(random_players, number)

        # Print de bijgewerkte kaart van de speler.
        print_layout(player_card, player_marked, current_number=number)  # Update het scherm na elke actie.

        # Check of de speler Bingo heeft.
        if check_bingo(player_card, player_marked):
            print("BINGO! Gefeliciteerd, je hebt gewonnen!")
            break

        # Check of een van de bots Bingo heeft.
        if any_random_player_has_bingo(random_players):
            print("Een van de andere deelnemers heeft Bingo! Het spel eindigt.")
            break

        # Wacht tot de speler op Enter drukt om verder te gaan.
        input("Druk op Enter om verder te gaan met het roepen van getallen...\n")

# Dit zorgt ervoor dat het spel begint als je het programma uitvoert.
if __name__ == "__main__":
    play_bingo()

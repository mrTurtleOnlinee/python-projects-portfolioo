# Functie voor optellen
def add(x, y):
    return x + y

# Functie voor aftrekken
def subtract(x, y):
    return x - y

# Functie voor vermenigvuldigen
def multiply(x, y):
    return x * y

# Functie voor delen
def divide(x, y):
    # Check of de gebruiker niet probeert te delen door 0
    if y == 0:
        return "Error: Kan niet delen door 0!"
    return x / y

# Functie om de keuze te verwerken en de juiste berekening uit te voeren
def calculator():
    print("Kies een bewerking:")
    print("1. Optellen")
    print("2. Aftrekken")
    print("3. Vermenigvuldigen")
    print("4. Delen")
    
    keuze = input("Maak een keuze (1/2/3/4): ")

    # Input van de gebruiker voor de getallen
    try:
        num1 = float(input("Voer het eerste nummer in: "))
        num2 = float(input("Voer het tweede nummer in: "))
    except ValueError:
        print("Error: Voer geldige getallen in.")
        return

    # Controleer welke operatie de gebruiker heeft gekozen en voer de juiste functie uit
    if keuze == "1":
        print(f"Resultaat: {num1} + {num2} = {add(num1, num2)}")
    elif keuze == "2":
        print(f"Resultaat: {num1} - {num2} = {subtract(num1, num2)}")
    elif keuze == "3":
        print(f"Resultaat: {num1} * {num2} = {multiply(num1, num2)}")
    elif keuze == "4":
        print(f"Resultaat: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Ongeldige keuze. Probeer opnieuw.")

# Functie om het programma te starten
if __name__ == "__main__":
    while True:
        calculator()
        doorgaan = input("Wil je nog een berekening doen? (ja/nee): ").lower()
        if doorgaan != "ja":
            print("Rekenmachine afgesloten.")
            break


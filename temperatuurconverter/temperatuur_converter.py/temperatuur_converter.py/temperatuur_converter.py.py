# Functie om Celsius naar Fahrenheit te converteren
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Functie om Fahrenheit naar Celsius te converteren
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Functie om de gebruiker te vragen welke conversie ze willen doen
def main():
    print("Temperatuur Converter")
    print("1. Converteer Celsius naar Fahrenheit")
    print("2. Converteer Fahrenheit naar Celsius")
    
    keuze = input("Maak een keuze (1 of 2): ")

    # Controleer wat de gebruiker wil doen en vraag om de juiste invoer
    if keuze == "1":
        try:
            celsius = float(input("Voer de temperatuur in Celsius in: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}C is gelijk aan {fahrenheit:.2f}F")  # Geen graden symbool
        except ValueError:
            print("Voer een geldig nummer in.")
    
    elif keuze == "2":
        try:
            fahrenheit = float(input("Voer de temperatuur in Fahrenheit in: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}F is gelijk aan {celsius:.2f}C")  # Geen graden symbool
        except ValueError:
            print("Voer een geldig nummer in.")
    
    else:
        print("Ongeldige keuze. Probeer opnieuw.")

# Start het programma
if __name__ == "__main__":
    main()

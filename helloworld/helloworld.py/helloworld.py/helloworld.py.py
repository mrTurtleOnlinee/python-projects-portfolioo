# Definieer een functie die een begroeting weergeeft
def greet_user(name):
    print(f"Hello, {name}! Welcome to the world of Python programming.")

# Definieer de hoofdfunctie van het programma
def main():
    print("Hello, World!")
    # Vraag om de naam van de gebruiker
    user_name = input("What is your name? ")

    # Roep de functie aan om de gebruiker te begroeten
    greet_user(user_name)

    # Een extra bericht om het programma af te sluiten
    print("This is a simple Python program that greets you.")
    print("Goodbye, and happy coding!")

# Controleer of dit het hoofdprogramma is en start het programma
if __name__ == "__main__":
    main()


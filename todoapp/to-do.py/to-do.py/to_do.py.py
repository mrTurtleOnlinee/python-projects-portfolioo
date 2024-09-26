import os

# Functie om taken op te slaan
def save_tasks(tasks, filename="todo_list.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

# Functie om taken te laden
def load_tasks(filename="todo_list.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    else:
        tasks = []
    return tasks

# Functie om taken weer te geven
def show_tasks(tasks):
    if not tasks:
        print("Geen taken op de lijst.")
    else:
        print("\nTo-do lijst:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Functie om een nieuwe taak toe te voegen
def add_task(tasks):
    task = input("Voer een nieuwe taak in: ")
    tasks.append(task)
    save_tasks(tasks)

# Functie om een taak als voltooid te markeren
def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_no = int(input("Welke taak wil je voltooien? Voer het nummer in: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks.pop(task_no)
            save_tasks(tasks)
            print("Taak voltooid en verwijderd van de lijst.")
        else:
            print("Ongeldig taaknummer.")
    except ValueError:
        print("Voer een geldig nummer in.")

# Functie om de lijst te tonen en keuzes te maken
def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Toon taken")
        print("2. Voeg taak toe")
        print("3. Markeer taak als voltooid")
        print("4. Afsluiten")
        
        choice = input("\nMaak een keuze: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Programma beeindigd.")  # Speciaal teken is verwijderd
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

if __name__ == "__main__":
    main()

import datetime

def write_entry():
    entry = input("Apni aaj ki diary likhiye: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("diary.txt", "a") as file:
        file.write(f"\n{date}:\n{entry}\n{'-'*30}")

def read_entries():
    try:
        with open("diary.txt", "r") as file:
            print("\n--- Diary Entries ---\n")
            print(file.read())
    except FileNotFoundError:
        print("Abhi tak koi entry nahi ki gayi.")

def menu():
    while True:
        print("\n1. Nayi Entry Likho")
        print("2. Sab Entries Dekho")
        print("3. Exit")
        choice = input("Apna choice do (1/2/3): ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Bye Bye!")
            break
        else:
            print("Sahi option chuno.")

menu()

fruit_list = []  # Start with an empty list

while True:
    print("\nOptions: add / remove / view / quit")
    action = input("What would you like to do? ").lower()

    if action == "add":
        fruit = input("Enter fruit to add: ")
        fruit_list.append(fruit)
        print(f"{fruit} added.")
    elif action == "remove":
        fruit = input("Enter fruit to remove: ")
        if fruit in fruit_list:
            fruit_list.remove(fruit)
            print(f"{fruit} removed.")
        else:
            print(f"{fruit} not found in the list.")
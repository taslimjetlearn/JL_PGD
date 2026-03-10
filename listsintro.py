names = []

while True:
    print("\nMenu")
    print("1. Add name")
    print("2. Change name")
    print("3. Delete name")
    print("4. View names")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter a name to add: ")
        names.append(name)

    elif choice == "2":
        print(names)
        i = int(input("Enter the position of the name to change: "))
        new_name = input("Enter the new name: ")
        names[i-1] = new_name

    elif choice == "3":
        print(names)
        i = int(input("Enter the position of the name to delete: "))
        names.pop(i-1)

    elif choice == "4":
        print("Names in list:", names)

    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Invalid option")
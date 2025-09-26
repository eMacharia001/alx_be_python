# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Explicit array

    while True:
        display_menu()  # Call the menu function

        choice = int(input("Enter your choice: "))  # Input as number

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(item, "added to the shopping list.")

        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(item, "removed from the shopping list.")
            else:
                print(item, "not found in the shopping list.")

        elif choice == 3:
            print("Shopping List:")
            for item in shopping_list:
                print(item)

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


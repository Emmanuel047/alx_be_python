def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add = input("Enter the item you want to add: ")
            shopping_list.append(add)
            pass
        elif choice == 2:
            # Prompt for and remove an item
            remove = input("Enter the name of the item you want to remove").lower()
            shopping_list.remove(remove)
            pass
        elif choice == 3:
            # Display the shopping list
            for i in shopping_list:
                print(i)
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
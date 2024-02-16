arr = []

# Function to insert an element into the array
def insert_element(element):
    arr.append(element)
    print("Element inserted successfully.")

# Function to delete an element from the array
def delete_element(element):
    if element in arr:
        arr.remove(element)
        print("Element deleted successfully.")
    else:
        print("Element not found in the array.")

# Function to update an element in the array
def update_element(index, element):
    if index < len(arr):
        arr[index] = element
        print("Element updated successfully.")
    else:
        print("Invalid index.")

# Function to search for an element in the array
def search_element(element):
    if element in arr:
        print("Element found in the array.")
    else:
        print("Element not found in the array.")

# Main function to take user choice of operation
def main():
    while True:
        print("\nSelect operation:")
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Search")
        print("5. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            element = input("Enter element to insert: ")
            insert_element(element)
        elif choice == 2:
            element = input("Enter element to delete: ")
            delete_element(element)
        elif choice == 3:
            index = int(input("Enter index to update: "))
            element = input("Enter new element: ")
            update_element(index, element)
        elif choice == 4:
            element = input("Enter element to search: ")
            search_element(element)
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

main()

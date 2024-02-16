stack = []

# Function to push an element onto the stack
def push(element):
    stack.append(element)
    print("Element pushed onto the stack.")

# Function to pop an element from the stack
def pop():
    if len(stack) > 0:
        stack.pop()
        print("Element popped from the stack.")
    else:
        print("Stack is empty.")

# Function to peek at the top element of the stack
def peep():
    if len(stack) > 0:
        print("Top element of the stack:", stack[-1])
    else:
        print("Stack is empty.")

# Function to change an element at a given index of the stack
def change(index, element):
    if index < len(stack):
        stack[index] = element
        print("Element at index", index, "is changed to", element)
    else:
        print("Invalid index.")

# Function to display the elements of the stack
def display():
    if len(stack) > 0:
        print("Elements of the stack:", stack)
    else:
        print("Stack is empty.")

# Main function to take user choice of operation
def main():
    while True:
        print("\nSelect operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peep")
        print("4. Change")
        print("5. Display")
        print("6. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            element = input("Enter element to push: ")
            push(element)
        elif choice == 2:
            pop()
        elif choice == 3:
            peep()
        elif choice == 4:
            index = int(input("Enter index to change: "))
            element = input("Enter new element: ")
            change(index, element)
        elif choice == 5:
            display()
        elif choice == 6:
            break
        else:
            print("Invalid choice.")

# Call the main function
if __name__ == '__main__':
    main()

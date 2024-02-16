import java.util.Scanner;

class Stack {
    int top = -1;
    int MAX = 10;
    int[] stack = new int[MAX];

    void push(int value) {
        if (top == MAX - 1) {
            System.out.println("Stack Overflow");
        } else {
            top++;
            stack[top] = value;
            System.out.println("Inserted value: " + value);
        }
    }

    void pop() {
        if (top == -1) {
            System.out.println("Stack Underflow");
        } else {
            System.out.println("Popped value: " + stack[top]);
            top--;
        }
    }

    void peep() {
        if (top == -1) {
            System.out.println("Stack is empty");
        } else {
            System.out.println("Top value: " + stack[top]);
        }
    }

    void change(int index, int value) {
        if (top - index + 1 < 0) {
            System.out.println("Invalid index");
        } else {
            stack[top - index + 1] = value;
            System.out.println("Value changed at index " + index + " to " + value);
        }
    }

    void display() {
        if (top == -1) {
            System.out.println("Stack is empty");
        } else {
            System.out.println("Stack values:");
            for (int i = top; i >= 0; i--) {
                System.out.println(stack[i]);
            }
        }
    }
}

public class Practical_3 {
    public static void main(String[] args) {
        Stack stack = new Stack();
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("\nSelect operation:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peep");
            System.out.println("4. Change");
            System.out.println("5. Display");
            System.out.println("6. Exit");
            int choice = sc.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter value: ");
                    int value = sc.nextInt();
                    stack.push(value);
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    stack.peep();
                    break;
                case 4:
                    System.out.print("Enter index: ");
                    int index = sc.nextInt();
                    System.out.print("Enter value: ");
                    value = sc.nextInt();
                    stack.change(index, value);
                    break;
                case 5:
                    stack.display();
                    break;
                case 6:
                    sc.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
    
}

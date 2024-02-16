import java.util.Scanner;

public class Practical_1 {

    static int[] array = new int[10];
    static int count = 0;
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("Please select an operation:");
            System.out.println("1. Insert");
            System.out.println("2. Delete");
            System.out.println("3. Update");
            System.out.println("4. Search");
            System.out.println("5. Exit");
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    insert();
                    break;
                case 2:
                    delete();
                    break;
                case 3:
                    update();
                    break;
                case 4:
                    search();
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void insert() {
        System.out.println("Enter the value to be inserted:");
        int value = scanner.nextInt();
        if (count == array.length) {
            System.out.println("Array is full. Cannot insert any more elements.");
        } else {
            array[count++] = value;
            System.out.println("Value inserted successfully.");
        }
    }

    private static void delete() {
        System.out.println("Enter the index of the element to be deleted:");
        int index = scanner.nextInt();
        if (index < 0 || index >= count) {
            System.out.println("Invalid index. Please try again.");
        } else {
            for (int i = index; i < count - 1; i++) {
                array[i] = array[i + 1];
            }
            count--;
            System.out.println("Value deleted successfully.");
        }
    }

    private static void update() {
        System.out.println("Enter the index of the element to be updated:");
        int index = scanner.nextInt();
        if (index < 0 || index >= count) {
            System.out.println("Invalid index. Please try again.");
        } else {
            System.out.println("Enter the new value:");
            int value = scanner.nextInt();
            array[index] = value;
            System.out.println("Value updated successfully.");
        }
    }

    private static void search() {
        System.out.println("Enter the value to be searched:");
        int value = scanner.nextInt();
        boolean found = false;
        for (int i = 0; i < count; i++) {
            if (array[i] == value) {
                System.out.println("Value found at index " + i);
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("Value not found in the array.");
        }
    }
}
/*Purv Devenbhai Joshi
  202103103510429
  Class:- CS-2
 */
import java.util.*;
public class Practical_8 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);	
		int[] numbers = new int[10];	
    for (int i = 0; i < numbers.length; i++){
            System.out.print("Enter numbers "+ (i+1) + ":");
			numbers[i] = input.nextInt();
        }
		reverse(numbers);
        for (int e: numbers) {
			System.out.print(e + " ");
		}
		System.out.println();
	}
	public static void reverse(int[] list) {
		int temp;
        System.out.println("\n");
        System.out.println("Numbers in reverse:");
		for (int i = 0, j = list.length - 1; i < list.length / 2; i++, j--) {
            temp = list[i];
			list[i] = list[j];
			list[j] = temp;
		}
	}
}




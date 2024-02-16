/*Purv Devenbhai Joshi
  202103103510429
 Class:- CS-2
 */
import java.util.*;
public class Practical_13 {
    public static void main(String[] args) {
        Scanner input =new Scanner(System.in);
        try{
            System.out.print("Enter number :");
            int num_1=input.nextInt();
            int num_2=0;
            int num_3=num_1/num_2;
            System.out.print(num_3);
        }
        catch(Exception e){
            System.out.println("Can not divided by zero!!!!");
        }
    }
}

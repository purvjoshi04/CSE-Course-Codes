/*Purv Devenbhai Joshi
  202103103510429
  Class:- CS-2
 */
/*Assume a vehicle plate number consists of three
uppercase letters followed by four digits. Write a
program to generate a plate number. */
import java.lang.Math; import java.util.Random;
class Practical_7{
    public static void main(String[]args){
            {
            Random num_random=new Random();
            char a=(char)(num_random.nextInt(26) + 65);
             char b=(char)(num_random.nextInt(26) + 65); 
             char c=(char)(num_random.nextInt(26) + 65); 
             int max = 9999; int min = 1000; 
             int range = max - min;
            int num_plate = (int)(Math.random() * range) + min;
            System.out.print((char)a);
            System.out.print((char)b);
            System.out.print((char)c);
            System.out.println(num_plate); 
            }
            }
            
    }

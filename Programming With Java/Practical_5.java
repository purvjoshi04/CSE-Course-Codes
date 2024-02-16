/*Write a program that prompts the user to enter a
letter and check whether a letter is a vowel or
consonant. */
import java.util.Scanner;
public class Practical_5{
public static void main(String [] args){
    Scanner alpha=new Scanner(System.in);
    System.out.print("Enter alphabet :");
    char ch=alpha.next().charAt(0);

if(ch=='A' ||ch== 'a' || ch=='E' || ch=='e' ||ch== 'I' || ch=='i'  ||ch== 'O' ||ch== 'o' || ch=='U'  || ch =='u'){
    System.out.println("The entered alphabet is vowel:");
}else{
    System.out.println("The entered alphabet is consonant");
}
    }
}

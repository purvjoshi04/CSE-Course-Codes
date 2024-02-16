//Write a program for calculator.

import java.util.Scanner;
public class Practical_2{
    public static void main(String [] args){
        Scanner num=new Scanner(System.in);
        System.out.print("Enter first number:");
        int a=num.nextInt();
        System.out.print("Enter second number:");
        int b=num.nextInt();
        System.out.print("\n");
        int add=a+b;
        int sub=a-b;
        int multi=a*b;
        int div=a/b;
        System.out.println("The Addition of two numbers is:"+add);
        System.out.println("The Subtractions of two numbers is:"+sub);
        System.out.println("The Multiplication of two numbers is:"+multi);
        System.out.println("The Division of two numbers is:"+div);
        }
}
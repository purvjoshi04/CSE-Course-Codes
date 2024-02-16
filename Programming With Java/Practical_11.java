/*Purv Devenbhai Joshi
  202103103510429
 Class:- CS-2
 */
import java.util.*;
abstract class Shape{
abstract void area();
double area;
}

class Triangle extends Shape{
double base=50,heigth=15;
void area(){
area = (base*heigth)/2;
System.out.println("area of Triangle ->"+area);
}
}

class Rectangle extends Shape{
double width=70,heigth=20;
void area(){
area = width*heigth;
System.out.println("area of Rectangle ->"+area);
}
}

class Circle extends Shape{
double radius=5;
void area(){
area = Math.PI * radius * radius;
System.out.println("area of Circle ->"+area);
}
}

public class Practical_11{
public static void main(String [] args){
Triangle tri_obj= new Triangle();
Rectangle rec_obj =new Rectangle();
Circle cir_obj=new Circle();

tri_obj.area();
rec_obj.area();
cir_obj.area();
}
}
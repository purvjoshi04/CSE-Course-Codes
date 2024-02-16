package pack_2;

import pack_1.Demo_1;

public class Demo_2 extends Demo_1{
   public void method(){
        System.out.println("Hello i am from class Demo_2");
    }
    public static void main(String[] args) {
        Demo_1 obj_1=new  Demo_1();
        obj_1.method();
    }
}

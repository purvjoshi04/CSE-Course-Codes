/*Purv Devenbhai Joshi
  202103103510429
 Class:- CS-2
 */
interface Student{
    void student_name();
}
interface Collage{
  
    void student_collage();
}
interface Age{
    void student_age();
}

class Practical_12 implements Student,Collage{
    public void student_name(){
        String std_name="Purv";
        System.out.println("Student name is "+std_name+".");
    }
   public void student_collage(){
    String std_collage="UKA TARSADIA";
        System.out.println("Student collage name is "+std_collage+".");
    }
    public void student_age(){
        int std_age=18;
        System.out.println("Student age is "+std_age+".");
    }

public static void main(String[] args) {
    Practical_12 obj=new Practical_12();
    obj.student_name();
    obj.student_collage();
    obj.student_age();
}
}
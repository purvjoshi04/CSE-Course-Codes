class Practical_14{
    public static void main(String[] args) {
    try{
    int num_1=0;
    int num_2=10;
    int num_3=num_2/num_1;
    System.out.println(num_3);
        try{
            int index[]=new int[2];
           index[2]=500;
            System.out.println(index[10]);
        }catch(IndexOutOfBoundsException e){
            System.out.println("Index out of bound exception.");
        }
    }catch(ArithmeticException e){
        System.out.println("Arithmatic exception.");
    }
}
}
  

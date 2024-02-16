/*Purv Devenbhai Joshi
  202103103510429
 Class:- CS-2
 */
import java.util.*;
public class Practical_9 {
   public static int[][] create_fill_matrix(){
  int [][]matrix = new int[6][6];
  for(int i=0;i<6;i++) {
   for(int j=0;j<6;j++){
    matrix[i][j]=(int)((Math.random()*6)%2);
   }
  }
  return matrix;
 }
 public static void displayMatrix(int [][]matrix){
  System.out.print("\nMatrix Values \n");
  for(int i=0;i<6;i++){
   for(int j=0;j<6;j++){
    System.out.print(matrix[i][j]+ " ");
   }
   System.out.println();
  }
 }
 public static void main(String[] args) {
  int my_matrix[][];
  int i,j,count;
  my_matrix=create_fill_matrix();
  displayMatrix(my_matrix);
  System.out.println("\nRows Having ODD no of 1s");
  for(i=0;i<6;i++)
  {
   count=0;
   for(j=0;j<6;j++)
   {
    if(my_matrix[i][j]==1)
    {
     count++;
    }
   }
   if(count%2!=0)
   {
    System.out.println("Row - "+(i+1)+" have ODD no of 1s");
   }
  }
  System.out.println("\nColumns Having ODD no of 1s");
  for(i=0;i<6;i++)
  {
   count=0;
   for(j=0;j<6;j++)
   {
    if(my_matrix[j][i]==1)
    {
     count++;
    }
   }
   if(count%2!=0)
   {
    System.out.println("Column - "+(i+1)+" have ODD no of 1s");
   }
  }
 }
}


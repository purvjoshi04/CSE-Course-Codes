import java.util.Scanner;
public class Practical_2 {
    public static void main(String[] args) {
      int array[][]={
                {0 , 0 , 6 , 0 , 9 },  
                {0 , 0 , 4 , 6 , 0 },  
                {0 , 0 , 0 , 0 , 0 },  
                {0 , 1 , 2 , 0 , 0 } 
               };
            int size=0;
            for(int i=0;i<4;i++){
              for(int j=0;j<5;j++){
                if(array[i][j]!=0){
                  size++;
                }
              }
            }
            int final_matrix[][]=new int[3][size];
            int k=0;
            for(int i=0;i<4;i++){
                for(int j=0;j<5;j++){
                  if(array[i][j]!=0){
                    final_matrix[0][k]=i;
                    final_matrix[1][k]=j;
                    final_matrix[2][k]=array[i][j];
                  k++;
                  }
                }
            }
            for(int i=0;i<3;i++){
              for(int j=0;j<size;j++){
                System.out.print(""+final_matrix[i][j]);
              }
              System.out.println("\n");
            }
            
          }
        }


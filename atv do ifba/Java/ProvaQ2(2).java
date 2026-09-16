import java.util.Scanner;

public class ProvaQ2 {
   public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    int[] N = new int[5];
     int soma = 0;

       int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

     for(int i = 0; i <= 4; i++){

        System.out.println("Coloque um numero inteiro de sua preferencia: ");
        N[i] = sc.nextInt();
        if(N[i] < min){
            min = N[i];
        }
        if(N[i] > max){
            max = N[i];
        }
        soma = soma+N[i];
    }
             Double media = soma/5.0;
             System.out.println("Valor mínmo: "+min);
             System.out.println("Valor máximo: "+max);
             System.out.println("Média: "+media);

    
    sc.close();
    }
}
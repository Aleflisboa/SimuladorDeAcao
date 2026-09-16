import java.util.Scanner;

public class Q4 {
    public static void main (String args []){
        try (Scanner sc = new Scanner(System.in)) {
            int A = 0;
            int impar = 0;
      
   for (A = 0; A >=0;) {
    System.out.println("Digite um numero positivo ou negativo: ");
       A = sc.nextInt();
      
       if (A % 2 != 0) {
       if (A > impar) {
          impar = A;
}
  }
   }
      
  System.out.println("O maior numero é: " + impar);
  sc.close();
        }
        
  }
}
        
    


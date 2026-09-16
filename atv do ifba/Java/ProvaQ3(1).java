import java.util.Scanner;

public class ProvaQ3 {
   public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    int Root = 1;
    System.out.println("Digite um número: ");
         Double N = sc.nextDouble();

    for( int i = 2; i <= N; i++ ){

        Root *= i;
    }
    System.out.println("Fatorial do número "+N+" = "+FatN);
    
    
    sc.close();
    }
}
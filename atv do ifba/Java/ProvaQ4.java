import java.util.Scanner;

public class ProvaQ4 {
   public static void main(String args[]) {
         Scanner sc = new Scanner(System.in);

    System.out.print("Coloque o valor do depósito do produto: ");
        Double Deposito = sc.nextDouble();
    
    System.out.print("Coloque a taxa de juros do produto: ");
         Double Juros = sc.nextDouble();
    
    double Redimento = Juros/100*(Deposito);
      Double total = Deposito+Redimento;
          
          System.out.println("Valor dos redimento: "+Redimento);
          System.out.println("Valor total: "+total);
    
    
    sc.close();
    }
}
import java.util.Scanner;

public class ProvaQ5 {
   public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Coloque um número: ");
         Double N = sc.nextDouble();
  
           if(N%3 == 0){
            System.out.println("O número requerido "+N+" é múltiplo de 3");
            } else{
        System.out.println("O número requerido "+N+" não é múltiplo de 3");
    }
    
     sc.close();
    }
}
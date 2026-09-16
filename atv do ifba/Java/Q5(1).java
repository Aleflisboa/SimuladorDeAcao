import java.util.Scanner;

public class Q5 {
    public static void main (String args []){
        try (Scanner sc = new Scanner(System.in)) {
    
            System.out.println("Qual o valor da bonificação");
            Float Beneficio = sc.nextFloat();
 
            System.out.println("Numero de funcionrios");
            int funcionario = sc.nextInt();

            double crédito_social = Beneficio / funcionario * 2;
		double credito_funcinario = (Beneficio - crédito_social) / funcionario;

        System.out.println("A quantidade que o socio ganhara sera:" + crédito_social);
		System.out.println("A quantidade que cada funcionario obteu foi:" + credito_funcinario);

		sc.close();
        } 
 }
}
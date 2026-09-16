import java.util.Scanner;

public class Q2 {
    public static void main (String args []){
		Scanner sc = new Scanner(System.in);

    System.out.println("Digite o valor do seu investimento: "); 
    double Investimento = sc.nextDouble();

    System.out.println("Digite tempo que deseja investir: ");
    int Tempo = sc.nextInt();

    double Rendimento = 0.0;

    for (int i = 0; i < Tempo; i++ ) {
        Rendimento += (Investimento / 100 * 0.5);

	}
      
    System.out.println("Remendiment: " + Rendimento);

		sc.close();

    }
}
		
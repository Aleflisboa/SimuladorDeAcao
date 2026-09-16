import java.util.Scanner;

public class Q2 {
    public static void main (String args []){
		Scanner sc = new Scanner(System.in);

    System.out.println("Digite o valor do seu investimento: "); 
    double Investimento = sc.nextDouble();

    System.out.println("Digite tempo que deseja investir: ");
    int Tempo = sc.nextInt();

    int Contabilização = 0;

    double Rendimento = Investimento * (0.5/100 * Tempo) + Investimento;

    while (Contabilização < Tempo) {
        Rendimento = (Investimento + (0.5 / 100) * Investimento);
			Investimento = Rendimento;
			Contabilização++;

			System.out.println("Retorno do Investimento "+ Contabilização + ": R$"  + Investimento);
		}

		sc.close();

    }
}
		
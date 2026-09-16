import java.util.Scanner;

public class Q1 {

	public static void main (String args []){
		Scanner sc = new Scanner(System.in);

		int contabilização = 0;
		int expoente = 7;
		int decimal = 0;
		int bits = sc.nextInt();

		double potencia = Math.pow(2, expoente);

		decimal += potencia * bits;
		contabilização++;
		expoente--;

		while(contabilização < 8) {
		System.out.println("Digite uma sequencia de 8 bits:");

		}

		System.out.println("A forma decimal é:" + decimal);

		sc.close();
	}
}
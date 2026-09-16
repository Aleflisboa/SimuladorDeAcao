import java.util.Scanner;
public class Q3 {
    public static void main (String args []){
		Scanner sc = new Scanner(System.in);

        System.out.println("Digite a quantidade litros de gasolina que deseja:");
		int litro = sc.nextInt();

        double gasolina = litro * 7.33;
		double redução_da_gasolina = gasolina - (gasolina / 100) * 5;

        double refinaria = redução_da_gasolina / 100 * 33.5;
        System.out.println("Lucro que a refinaria possui:" + refinaria);

		double impostos_federais = redução_da_gasolina / 100 * 11.3;
        System.out.println("Lucro que os impostos federais possui:" + impostos_federais);

        double etanol_anidro = redução_da_gasolina / 100 * 17;
        System.out.println("Lucro que a etanol anidro possui:" + etanol_anidro);

		double impostos_estaduais = redução_da_gasolina / 100 * 27.6;
        System.out.println("Lucro que os impostos etaduais possui:" + impostos_estaduais);

        double distribuidora = redução_da_gasolina / 100 * 10.6;
        System.out.println("Lucro que a distribuidora possui:" + distribuidora);

        sc.close();
    }
}

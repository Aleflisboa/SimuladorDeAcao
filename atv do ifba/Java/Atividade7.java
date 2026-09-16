package OHAMA;

import java.util.Scanner;
public class Atividade7 {
public static void main(String[] args) {
    Scanner s = new Scanner(System.in);

System.out.println("Vamos dividir!");

System.out.println("Digite o primeiro valor: ");
int x = s.nextInt();

System.out.println("Digite o segundo valor: ");
int y = s.nextInt();
	
try {
    double r = (x / y);
    System.out.println("Resultado: " + r);
    
} catch (ArithmeticException e){
    System.out.println("Erro: não foi possivel fazer essa operção");
    e.getMessage();
    
    while (y == 0) {
        System.out.println("Digite o valor de Y novamente");
        y = s.nextInt();
    }
    
    double r = (x / y);
    System.out.println("Operção sucedida, esse é valor resultado: " + r);
    
}

 s.close();

  }
}

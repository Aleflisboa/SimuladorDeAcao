package OHAMA;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;


public class Atividade3 {
    
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        int num = 0;
        int soma = 0;
        int produto = 1;

        while(0 <= num && num < 100) {
            System.out.println("Digite numeros positivos, caso queira parar digite numero negativo ou maior que 100");
            num = sc.nextInt();

        if (0 <= num && num < 100){
            soma += num;
            produto *= num;
        }
    }

        FileWriter escrever = new FileWriter("Quest3.txt");
        PrintWriter gravar = new PrintWriter(escrever);

        for (int i = 0; i < 1; i++);{
            gravar.println(produto);
            gravar.println(soma);
        }

       System.out.println("Fim");

       
       gravar.close();
       sc.close();
    }
}

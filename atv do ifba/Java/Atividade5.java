package OHAMA;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Atividade5 {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        int X = 0;
        int Y = 0;
        int Resto = 0;

        System.out.println("Digite um valor para X");
        X = sc.nextInt();

        System.out.println("Digite um Valor para Y");
        Y = sc.nextInt();

        while (Y != 0) {
            Resto = X % Y;
            X = Y;
            Y = Resto;

        }

        FileWriter Arquivo = new FileWriter("Quest5.txt");
        PrintWriter Gravar = new PrintWriter(Arquivo);

        for (int i = 0; i < 1; i++ );{
            Gravar.println(X);

        }

    Gravar.close();
    sc.close();
 }
}
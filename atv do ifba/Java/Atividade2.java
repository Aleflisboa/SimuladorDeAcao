package OHAMA;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Atividade2 {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        FileWriter c1 = new FileWriter(Resultado.txt);
        FileReader c2 = new FileReader(Quest2.txt);
        BufferedReader c3 = new BufferedReader(c2);
        PrintWriter c4 = new PrintWriter(c1);

        String in1 = c3.readLine();
        double num1 = Double.parseDouble(in1);
        in1 = c3.readLine();
        double num2 = Double.parseDouble(in1);

        double soma = num1 + num2;
        double sub = num1 - num2;
        double mut = num1 * num2;
        double div = 0;
        try{
            div = num1/num2;
        } catch (ArithmeticException e){
            System.out.println("Não foi posivel continuar com essa operação");
        }
        
        double resto = num1 % num2;
    
        c4.println(soma);
        c4.println(sub);
        c4.println(mut);
        c4.println(div);
        c4.println(resto);

        c1.close();
        c2.close();
        c3.close();
        c4.close();
}
}

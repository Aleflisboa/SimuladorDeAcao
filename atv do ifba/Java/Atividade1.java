package OHAMA;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Atividade1 {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        FileWriter c1 = new FileWriter("CR7.txt");
        PrintWriter c2 = new PrintWriter(c1);

        c2.printf("nome: Alef de Jesus\n Data de Nascimento: 31/07/1980\n Naturalidade: Bahia\n Nacionalidade\n Matricula: 20011234-5");
    
    c1.close();
    c2.close();
    sc.close();
    
    }
}



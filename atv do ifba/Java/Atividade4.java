package OHAMA;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Atividade4 {
    public static void main(String[] args) throws IOException{
     Scanner sc = new Scanner(System.in);
     
     int Valor = 0;
     int maiorV = 0;
     int menorV = Integer.MAX_VALUE;
     int Media = 0;
     int soma = 0;
     int cont = 0;

     while(0 <= Valor && Valor < 1000000) {
     System.out.println("Digite os Numeros positivo, caso queira parar digite um numero negativo");
     Valor = sc.nextInt();

     if (Valor > maiorV){
        maiorV = Valor;
     }else if(0 <= Valor && Valor < menorV){
        menorV = Valor;
     }
     if(0 <= Valor && Valor < 1000000){
        soma += Valor;
        cont ++;
     }

    
     }
     Media = soma / cont;

     FileWriter escrever = new FileWriter("Quest4.txt");
     PrintWriter gravar = new PrintWriter(escrever);


     for (int i = 0; i < 1; i++){
     gravar.println(maiorV);
     gravar.println(menorV);
     gravar.println(Media);
 
     gravar.close();
     sc.close();
     
   }
 }
}

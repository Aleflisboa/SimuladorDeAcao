
import java.util.Scanner;

public class Conta{
	
    Scanner sc = new Scanner(System.in);
    protected double valorsacar;
    protected Double valordeposito;
    protected double saldo;

    public void sacar(){
    	
        System.out.println("Digite um valor para sacar");
        valorsacar = sc.nextDouble();
        this.saldo = this.saldo - valorsacar;
    }

     public void depositar(){
        System.out.println("Digite um valor para deposito");
        valordeposito = sc.nextDouble();
        this.saldo = this.saldo + valordeposito;
    
     }
}
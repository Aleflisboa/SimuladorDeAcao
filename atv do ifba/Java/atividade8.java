
public class atividade8 {

	public static void main(String[] args) {
		Conta c = new Conta();

		try {
			c.depositar();
	        c.sacar();
	        
	        if(c.saldo < 0) {
	        	throw new ContaExcecao(c.saldo, 0);
	        }else {
	        	System.out.println("Seu saldo: " + c.saldo);
	        }
		}catch(ContaExcecao e) {
			System.out.println("não foi possivel sacar");
		}
        
        
	}

}

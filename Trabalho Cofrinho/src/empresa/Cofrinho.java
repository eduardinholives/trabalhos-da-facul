package empresa;

import java.util.ArrayList;

public class Cofrinho {
	private ArrayList<Moedas> listaMoedas = new ArrayList <Moedas>();
	
	public void adicionar(Moedas m) {
		listaMoedas.add(m);
	}
	public void remover(Moedas m) {
		listaMoedas.remove(m);
	}
	public void listar() {
		for (Moedas m : listaMoedas) {
			System.out.println(m);
		}	
}
	public double converterValor() {
	

		double valorTotal =0;
		if(this.listaMoedas.isEmpty()) {
			return 0;
		}
		
		for(Moedas moeda : this.listaMoedas) {
			valorTotal = valorTotal + moeda.converterValor();
	}
		
		return valorTotal;
	}
		
	}

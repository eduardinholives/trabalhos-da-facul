package empresa;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		int opcao;
		
		Cofrinho cofrinho = new Cofrinho();
		
		System.out.println("Menu");
		System.out.println("1-Adicionar");
		System.out.println("2-Remover");
		System.out.println("3-Listar");
		System.out.println("4-Total convertido");
		System.out.println("0-Encerrar");
		opcao=teclado.nextInt();
		int tipoMoeda=0;
		double valor;
		Moedas moeda;
		
		while(opcao!=0) {
			
			switch(opcao) {
			
			case 1:
				tipoMoeda=0;
				while(tipoMoeda>3 || tipoMoeda<=00 ) {
					System.out.println("1-Real");
					System.out.println("2-Dolar");
					System.out.println("3-Euro");
					tipoMoeda = teclado.nextInt();
				}
				
				moeda=null;
				if(tipoMoeda==1) {
					System.out.println("Qual o valor da moeda?");
					valor = teclado.nextDouble();
					moeda = new Real(valor);
				}
				if(tipoMoeda==2) {
					System.out.println("Qual o valor da moeda?");
					 valor = teclado.nextDouble();
					moeda = new Dolar(valor);
				}
				if(tipoMoeda==3) {
					System.out.println("Qual o valor da moeda?");
					valor = teclado.nextDouble();
					moeda = new Euro(valor);
				}
				
				cofrinho.adicionar(moeda);
				
				break;
			case 2:
				tipoMoeda=0;
				while(tipoMoeda>3 || tipoMoeda<=00 ) {
					System.out.println("1-Real");
					System.out.println("2-Dolar");
					System.out.println("3-Euro");
					tipoMoeda = teclado.nextInt();
				}
				
				moeda=null;
				if(tipoMoeda==1) {
					System.out.println("Qual o valor da moeda?");
					valor = teclado.nextDouble();
					moeda = new Real(valor);
				}
				if(tipoMoeda==2) {
					System.out.println("Qual o valor da moeda?");
					valor = teclado.nextDouble();
					moeda = new Dolar(valor);
				}
				if(tipoMoeda==3) {
					System.out.println("Qual o valor da moeda?");
					valor = teclado.nextDouble();
					moeda = new Euro(valor);
				}
				
				cofrinho.remover(moeda);
				
				break;
			case 3:
				cofrinho.listar();
				break;
			case 4:
				double valorTotal = cofrinho.converterValor();
				System.out.println("O valor total em R$: " + valorTotal);
				break;
			default:
				System.out.println("Opção Inválida");
			}
			System.out.println("Menu");
			System.out.println("1-Adicionar");
			System.out.println("2-Remover");
			System.out.println("3-Listar");
			System.out.println("4-Total em R$");
			System.out.println("0-Encerrar");
			opcao=teclado.nextInt();
		}

	}

}

package empresa;

public class Dolar extends Moedas {

	public Dolar(double valor) {
		super(valor);
	}

	@Override
	public double converterValor() {
		return this.valor *5.15;
		
	}

	@Override
	public String toString() {
		return "US$ = " + valor ;
	}


	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		return true;
	}

}

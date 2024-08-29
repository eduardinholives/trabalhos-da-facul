package empresa;

public class Real extends Moedas {

	public Real(double valor) {
		super(valor);
		
	}

	@Override
	public double converterValor() {
		return this.valor;
		
	}

	@Override
	public String toString() {
		return "R$ = " + valor ;
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

package empresa;

public class Euro extends Moedas {


	public Euro(double valor) {
		super(valor);
	}

	@Override
	public double converterValor() {
		return this.valor*5.56;

	}

	public String toString() {
		return "€ = " + valor ;
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

package empresa;

import java.util.Objects;

public abstract class Moedas {
	double valor;
	
	
	abstract double converterValor();


	public Moedas(double valor) {
		super();
		this.valor = valor;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Moedas other = (Moedas) obj;
		return Double.doubleToLongBits(valor) == Double.doubleToLongBits(other.valor);
	}


	public double getValor() {
		return valor;
	}


	public void setValor(double valor) {
		this.valor = valor;
	}



	
}
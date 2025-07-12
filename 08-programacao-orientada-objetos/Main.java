// Classe base
class Veiculo {
    String marca;
    String modelo;
    int ano;

    public Veiculo(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }

    public void exibirInformacoes() {
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Ano: " + ano);
    }

    public void mover() {
        System.out.println("O veículo está se movendo.");
    }
}

// Subclasse Carro
class Carro extends Veiculo {
    int portas;

    public Carro(String marca, String modelo, int ano, int portas) {
        super(marca, modelo, ano);
        this.portas = portas;
    }

    @Override
    public void mover() {
        System.out.println("O carro está dirigindo na estrada.");
    }
}

// Subclasse Moto
class Moto extends Veiculo {
    boolean temPartidaEletrica;

    public Moto(String marca, String modelo, int ano, boolean temPartidaEletrica) {
        super(marca, modelo, ano);
        this.temPartidaEletrica = temPartidaEletrica;
    }

    @Override
    public void mover() {
        System.out.println("A moto está acelerando.");
    }
}

// Subclasse Bicicleta
class Bicicleta extends Veiculo {
    int marchas;

    public Bicicleta(String marca, String modelo, int ano, int marchas) {
        super(marca, modelo, ano);
        this.marchas = marchas;
    }

    @Override
    public void mover() {
        System.out.println("A bicicleta está pedalando.");
    }
}

// Classe principal
public class Main {
    public static void main(String[] args) {
        Carro carro = new Carro("Toyota", "Corolla", 2020, 4);
        Moto moto = new Moto("Honda", "CG 160", 2022, true);
        Bicicleta bicicleta = new Bicicleta("Caloi", "Explorer", 2021, 21);

        System.out.println("--- CARRO ---");
        carro.exibirInformacoes();
        carro.mover();

        System.out.println("\n--- MOTO ---");
        moto.exibirInformacoes();
        moto.mover();

        System.out.println("\n--- BICICLETA ---");
        bicicleta.exibirInformacoes();
        bicicleta.mover();
    }
}

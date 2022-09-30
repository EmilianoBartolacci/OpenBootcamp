// Bartolacci Emiliano
// Ejercicios tema 3 segunda parte

public class Main {
    public static void main(String[] args) {
        
        Coche miCoche = new Coche();
        miCoche.AumentarPuertas();

        System.out.println(miCoche.puertas);
    }
}

class Coche {
    public int puertas = 4;
    public void AumentarPuertas() {
        this.puertas++;
    }
}

// output = 5

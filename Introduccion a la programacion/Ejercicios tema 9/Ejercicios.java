// Bartolacci Emiliano
// Ejercicios tema 9

public class Main {
    public static void main(String[] args) {
        // creamos objetos y los imprimimos
        Cliente cliente = new Cliente();
        cliente.edad = 20;
        cliente.telefono = 502995;
        cliente.nombre = "Emiliano";
        cliente.credito = 0;

        System.out.println(cliente.edad);
        System.out.println(cliente.telefono);
        System.out.println(cliente.nombre);
        System.out.println(cliente.credito);

        Trabajador trabajador = new Trabajador();
        trabajador.edad = 26;
        trabajador.telefono = 502998;
        trabajador.nombre = "Mario";
        trabajador.salario = 25000;

        System.out.println(trabajador.edad);
        System.out.println(trabajador.telefono);
        System.out.println(trabajador.nombre);
        System.out.println(trabajador.salario);
    }
}

class Persona {
    int edad;
    String nombre;
    int telefono;
}

// creamos herencias de la clase Persona
class Cliente extends Persona {
    int credito;
}

class Trabajador extends Persona {
    int salario;
}

// output =
// 20
// 502995
// Emiliano
// 0
// 26
// 502998
// Mario
// 25000

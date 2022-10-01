// Bartolacci Emiliano
// Ejercicios tema 8

public class Main {
    public static void main(String[] args) {
        // creamos objeto e imprimimos
        Persona persona = new Persona();
        persona.setEdad(20);
        persona.setNombre("Emiliano");
        persona.setTelefono(502995);

        System.out.println(persona.getEdad());
        System.out.println(persona.getNombre());
        System.out.println(persona.getTelefono());
    }
}
class Persona {
    // creamos variables privadas y asignamos sets y gets
    private int edad;
    private String nombre;
    private int telefono;

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public int getTelefono() {
        return this.telefono;
    }
}

// output =
// 20
// Emiliano
// 502995

// Bartolacci Emiliano
// Ejercicios tema 4

public class Main {
    public static void main(String[] args) {
        int numeroIf = 3;
        if (numeroIf > 0) {
            System.out.print("numeroIf es positivo");
        } else if (numeroIf < 0) {
            System.out.print("numeroIf es negativo");
        } else if (numeroIf == 0) {
            System.out.print("numeroIf es 0");
        }

        int numeroWhile = 0;

        while (numeroIf < 3) {
            System.out.println(numeroWhile);
            numeroWhile++;
        }

        int numeroDoWhile = 0;

        do {
            System.out.println(numeroDoWhile);
            numeroDoWhile++;
        } while (numeroDoWhile < 3);

        for (var numeroFor = 0; numeroFor <= 3; numeroFor++) {
            System.out.println(numeroFor);
        }

        var estacion = "VERANO";

        switch (estacion) {
            case "VERANO":
                System.out.println("estamos en verano");
                break;
            case "INVIERNO":
                System.out.println("estamos en invierno");
                break;
            case "OTOÑO":
                System.out.println("estamos en otoño");
                break;
            case "PRIMAVERA":
                System.out.println("estamos en primavera");
                break;
            default:
                System.out.println("no es una estacion del año");
        }
    }
}

// output = 
// numeroIf es positivo
// 0
// 1
// 2
// 0
// 1
// 2
// 3
// estamos en verano

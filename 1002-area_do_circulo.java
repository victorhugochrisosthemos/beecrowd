import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
       Scanner scanner = new Scanner(System.in);

        // Leitura do valor de entrada
        double raio = scanner.nextDouble();

        // Cálculo da área
        double area = Math.pow(raio, 2) * 3.14159;

        // Exibição do resultado formatado
        System.out.printf("A=%.4f%n", area);

        scanner.close();
    }
 
}

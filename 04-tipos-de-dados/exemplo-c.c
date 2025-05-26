// Exemplo em C – Tipagem Estática e Forte
#include <stdio.h>

int main() {
    int x = 10;
    float y = 3.5;

    // x = "texto"; // Erro de compilação: tipo incompatível
    printf("Soma: %f\n", x + y); // Conversão implícita: int para float
    return 0;
}

//Exige declaração explícita de tipos. O tipo `int` é convertido para `float` ao somar com variável `y`.

#include <stdio.h>
#include <stdlib.h>

void dobrar(int *numero) {
    *numero = (*numero) * 2;
    printf("Dentro da funcao: numero = %d\n", *numero);
}

int main() {
    int valor = 10;

    printf("Antes da funcao: valor = %d\n", valor);

    dobrar(&valor);

    printf("Depois da funcao: valor = %d\n", valor);

    return 0;
}
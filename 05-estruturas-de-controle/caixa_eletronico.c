#include <stdio.h>

// Variável global para armazenar o saldo
float saldo = 1000.0;  // Saldo inicial fictício

void mostrarMenu();
void verSaldo();
void sacar();
void depositar();
void transferir();

int main() {
    int opcao;

    printf("Bem-vindo ao Caixa Eletrônico!\n");

    do {
        mostrarMenu();
        printf("\nEscolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                verSaldo();
                break;
            case 2:
                sacar();
                break;
            case 3:
                depositar();
                break;
            case 4:
                transferir();
                break;
            case 5:
                printf("Obrigado por usar o caixa eletrônico. Até logo!\n");
                break;
            default:
                printf("Opção inválida. Tente novamente.\n");
        }

    } while (opcao != 5);

    return 0;
}

void mostrarMenu() {  // Exibe o menu principal
    printf("\n=== Menu ===\n");
    printf("1. Ver saldo\n");
    printf("2. Sacar\n");
    printf("3. Depositar\n");
    printf("4. Transferir\n");
    printf("5. Sair\n");
}

void verSaldo() { // Mostra o saldo atual
    printf("\nSeu saldo atual é: R$ %.2f\n", saldo);
}

void sacar() { // realiza um saque com validação
    float valor;
    printf("\nDigite o valor para saque: R$ ");
    scanf("%f", &valor);

    if (valor <= 0) {
        printf("Valor inválido.\n");
    } else if (valor > saldo) {
        printf("Saldo insuficiente.\n");
    } else {
        saldo -= valor;
        printf("Saque de R$ %.2f realizado com sucesso.\n", valor);
        printf("Saldo restante: R$ %.2f\n", saldo);
    }
}

void depositar() { // realiza um depósito com validação
    float valor;
    printf("\nDigite o valor para depósito: R$ ");
    scanf("%f", &valor);

    if (valor <= 0) {
        printf("Valor inválido.\n");
    } else {
        saldo += valor;
        printf("Depósito de R$ %.2f realizado com sucesso.\n", valor);
        printf("Novo saldo: R$ %.2f\n", saldo);
    }
}

void transferir() { // Simula uma transferência para outra conta
    float valor;
    char conta[20];

    printf("\nDigite o número da conta de destino: ");
    scanf("%s", conta);
    printf("Digite o valor para transferência: R$ ");
    scanf("%f", &valor);

    if (valor <= 0) {
        printf("Valor inválido.\n");
    } else if (valor > saldo) {
        printf("Saldo insuficiente.\n");
    } else {
        saldo -= valor;
        printf("Transferência de R$ %.2f para a conta %s realizada com sucesso.\n", valor, conta);
        printf("Saldo restante: R$ %.2f\n", saldo);
    }
}

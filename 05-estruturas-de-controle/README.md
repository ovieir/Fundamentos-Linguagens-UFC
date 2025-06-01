# Desafio 05 – Estruturas de Controle

## Descrição do Desafio

Este desafio tem como objetivo aplicar **estruturas de controle de fluxo**, **seleção** e **repetição** em um programa com contexto prático e original.

Foi desenvolvido um **simulador completo de caixa eletrônico**, utilizando linguagem C, que oferece ao usuário a possibilidade de consultar saldo, sacar, depositar, transferir valores e sair do sistema por meio de um menu interativo.

---

## Funcionalidades Implementadas

- ✔ Ver saldo
- ✔ Saque com verificação de saldo
- ✔ Depósito com validação de valor
- ✔ Transferência simulada para outra conta
- ✔ Menu com loop de execução contínua
- ✔ Encerramento seguro da aplicação

---

## Técnicas Aplicadas

### ✅ Estruturas de Seleção
- `if`, `else`, `else if` para validações de entrada, saldo, etc.
- `switch` para controle das opções do menu

### ✅ Estruturas de Repetição
- `do...while` para manter o menu em execução até que o usuário opte por sair

### ✅ Controle de Fluxo
- `break` para encerrar o programa
- `return` ao fim do `main`
- Separação de lógica em **funções específicas** para modularização

---

## Estrutura do Código

O código está dividido em funções para melhor organização:

```c
void mostrarMenu();
void verSaldo();
void sacar();
void depositar();
void transferir();

```

---

## Referências

- SEBESTA, Robert W. *Conceitos de Linguagens de Programação*. 11ª ed. Pearson, 2018.
- KERNIGHAN, Brian W.; RITCHIE, Dennis M. *Linguagem de Programação C*. 2ª ed. São Paulo: Makron Books, 1995.
- [Documentação da linguagem C – cplusplus.com](https://cplusplus.com/)
- [DevDocs - C language reference](https://devdocs.io/c/)
- Notas de aula da disciplina *Linguagens de Programação* – Prof. Bruno de Castro.
---

## Autoria

Desenvolvido por Antonia Fabiana Rodrigues Oliveira  
**Disciplina:** Linguagens de Programação  
**Curso:** Sistemas de Informação  
**Instituição:** Universidade Federal do Ceará - UFC

---

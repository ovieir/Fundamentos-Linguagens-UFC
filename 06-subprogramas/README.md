# Desafio 06 – Subprogramas

## Objetivo

Este desafio tem como objetivo demonstrar dois modos de passagem de parâmetros em subprogramas:

- **Passagem por valor**  
- **Passagem por referência**

As implementações foram feitas em **linguagens diferentes**, conforme exigido no enunciado do trabalho: **Python** e **C**.

---

## Conceitos Fundamentais

### O que é um subprograma?

Um **subprograma** é um bloco de código reutilizável, com nome próprio, que pode receber entradas (parâmetros) e retornar saídas. Também pode ser chamado de **função, procedimento ou método**, dependendo da linguagem.

### Passagem de parâmetros

Ao chamar um subprograma, podemos enviar informações por:

| Tipo                     | Explicação                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| **Por valor**            | Uma **cópia** do valor é passada. Alterações dentro da função **não afetam** o original. |
| **Por referência**       | Um **endereço de memória** é passado. A função pode **alterar diretamente** o valor original. |

---

## Exemplo 1 – Passagem por Valor (Python)

**Arquivo:** `por_valor.py`

```python
def dobrar(numero):
    numero = numero * 2
    print("Dentro da função: número =", numero)

valor = 10
print("Antes da função: valor =", valor)
dobrar(valor)
print("Depois da função: valor =", valor)

```

## Exemplo 2 – Passagem por Referência (C)

**Arquivo:** `por_referencia.c`

``` c
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
```
---

## Referências
Apostila da disciplina – LIP AULA 6: Subprogramas, Prof. Bruno Honorato, UFC Crateús.
Sebesta, R. W. Conceitos de Linguagens de Programação – Capítulo 9 (Subprogramas).

---
## Autoria

- Aluna: Antonia Fabiana Rodrigues Oliveira
- Disciplina: Linguagens de Programação.
- Professor: Bruno Honorato – Universidade Federal do Ceará (UFC).
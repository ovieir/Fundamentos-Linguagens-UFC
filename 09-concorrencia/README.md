# Desafio 9 – Concorrência

## Objetivo

Este desafio tem como propósito compreender e demonstrar na prática o conceito de concorrência em linguagens de programação, abordando a diferença entre threads e processos e apresentando um exemplo funcional.

---

## Diferença entre Threads e Processos

### Processos
- São programas independentes em execução.
- Cada processo possui seu **próprio espaço de memória**.
- São mais seguros, pois não compartilham memória, mas isso também os torna mais lentos para comunicação entre si.

### Threads
- São unidades menores de execução **dentro de um mesmo processo**.
- Compartilham o **mesmo espaço de memória**, o que permite comunicação mais rápida, mas exige cuidado com sincronização de dados.
- São mais leves e eficientes para tarefas simultâneas que compartilham informações.

### Comparativo Rápido

| Aspecto          | Processos              | Threads                   |
|------------------|------------------------|---------------------------|
| Memória          | Isolada                | Compartilhada             |
| Custo de criação | Alto                   | Baixo                     |
| Comunicação      | Mais complexa          | Mais rápida               |
| Segurança        | Alta (isolamento)      | Menor (compartilhamento)  |
| Uso comum        | Execução de apps distintos | Tarefas paralelas no mesmo app |

---

## Exemplo Prático: Impressão Concorrente de Números Pares e Ímpares

Neste exemplo, utilizamos duas threads para executar, de forma concorrente, a impressão dos números pares (de 0 a 8) e dos números ímpares (de 1 a 9). Cada thread representa uma função distinta que simula uma tarefa independente com atraso (`sleep`) para evidenciar a execução simultânea.

A implementação foi feita em Python utilizando a biblioteca `threading`.

--- 

## Estrutura
O arquivo `concorrencia.py`, contém o código-fonte com a implementação da solução proposta.

---

## Saída esperada

- Ímpar: 1
- Par: 0
- Par: 2
- Ímpar: 3
- Ímpar: 5
- Par: 4
- Par: 6
- Ímpar: 7
- Par: 8
- Ímpar: 9
- Execução concorrente finalizada.

--- 

## Referências
- SEBESTA, Robert W. Conceitos de Linguagens de Programação. 10ª ed. Pearson, 2011.
- Documentação oficial do Python – Threading: https://docs.python.org/3/library/threading.html
- GUPTA, Aditya. Difference between Process and Thread. GeeksforGeeks. Disponível em: https://www.geeksforgeeks.org/difference-between-process-and-thread/

---

## Autoria
- Aluna: Antonia Fabiana Rodrigues Oliveira
- Disciplina: Linguagens de Programação
- Professor: Bruno Honorato – Universidade Federal do Ceará (UFC).

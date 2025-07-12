# Desafio 9 – Concorrência

## Objetivo

Este desafio tem como propósito compreender e demonstrar na prática o conceito de concorrência em linguagens de programação, abordando a diferença entre threads e processos e apresentando um exemplo funcional.

---

## Diferença entre Threads e Processos

## Processos

- São programas independentes em execução.
- Cada processo possui seu **próprio espaço de memória**.
- São mais seguros, pois não compartilham memória, mas isso também os torna mais lentos para comunicação entre si.

## Threads

- São unidades menores de execução **dentro de um mesmo processo**.
- Compartilham o **mesmo espaço de memória**, o que permite comunicação mais rápida, mas exige cuidado com sincronização de dados.
- São mais leves e eficientes para tarefas simultâneas que compartilham informações.

## Comparativo Rápido

| Aspecto        | Processos           | Threads              |
|----------------|---------------------|----------------------|
| Memória        | Isolada             | Compartilhada        |
| Custo de criação | Alto                | Baixo                |
| Comunicação    | Mais complexa       | Mais rápida          |
| Segurança      | Alta (isolamento)   | Menor (compartilhamento) |
| Uso comum      | Execução de apps distintos | Tarefas paralelas no mesmo app |

---

## Exemplo Prático: Envio de E-mails e Geração de Relatórios

Neste exemplo, simulamos duas tarefas concorrentes:

1. Uma função que envia 5 e-mails.
2. Outra que gera 3 relatórios.

As duas tarefas são executadas **simultaneamente usando threads**, por meio da biblioteca `threading` do Python. Isso demonstra como múltiplas ações podem ser executadas paralelamente para otimizar o tempo.

##  Arquivo: `email_relatorio.py`

A execução intercalada mostra o funcionamento da concorrência:

```bash
[Email] Enviando e-mail 1...
[Relatório] Gerando relatório 1...
[Email] Enviando e-mail 2...
...
[Relatório] Todos os relatórios foram gerados.
[Email] Todos os e-mails foram enviados.
```

--- 

## Referências
- SEBESTA, Robert W. Conceitos de Linguagens de Programação. 10ª ed. Pearson, 2011.
- Documentação oficial do Python – Threading: https://docs.python.org/3/library/threading.html
- GUPTA, Aditya. Difference between Process and Thread. GeeksforGeeks. Disponível em: https://www.geeksforgeeks.org/difference-between-process-and-thread/

---

## Autoria
- Aluna: Antonia Fabiana Rodrigues Oliveira
- Disciplina: Linguagens de Programação
- Professor: Bruno Honorato – Universidade Federal do Ceará (UFC)

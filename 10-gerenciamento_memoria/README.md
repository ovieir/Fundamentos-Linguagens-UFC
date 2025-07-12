# Desafio 10 – Gerenciamento de Memória

## Objetivo

O objetivo deste desafio é compreender como diferentes linguagens de programação lidam com o gerenciamento de memória, analisando os mecanismos utilizados, as responsabilidades do programador e os impactos no desempenho e na segurança da aplicação. Para isso, foi realizado um comparativo entre as linguagens **C** e **Java**.

---

## O que é Gerenciamento de Memória?

Gerenciamento de memória é o processo de alocação, uso e liberação de espaço na memória durante a execução de um programa. Um gerenciamento eficiente é essencial para garantir:
- O bom uso dos recursos do sistema;
- A prevenção de erros como vazamentos de memória ou corrupção de dados;
- O desempenho e estabilidade do software.

Existem dois tipos principais:
- **Manual**: o programador é responsável por alocar e liberar a memória (ex: C).
- **Automático**: o sistema libera a memória automaticamente quando ela não é mais necessária, por meio de um mecanismo chamado **Garbage Collector** (ex: Java).

---

## Análise das Linguagens

### C (Gerenciamento Manual)

Na linguagem C, o programador tem controle total sobre a memória. É necessário utilizar funções como:
- `malloc()` – aloca memória;
- `calloc()` – aloca e inicializa;
- `free()` – libera a memória alocada.

Apesar de oferecer alto desempenho e controle, essa abordagem exige cuidado, pois esquecer de liberar memória pode causar **vazamentos**.

### Java (Gerenciamento Automático)

Java utiliza **Garbage Collector (GC)**, que é responsável por liberar automaticamente a memória de objetos que não estão mais sendo utilizados. O programador não precisa (e não pode) liberar memória manualmente.

Embora facilite o desenvolvimento, o GC pode impactar o desempenho, especialmente se for executado em momentos críticos da aplicação.

---

## Quadro Comparativo

| Aspecto                      | C (Manual)                               | Java (Automático)                        |
|-----------------------------|------------------------------------------|------------------------------------------|
| Tipo de gerenciamento       | Manual (`malloc` / `free`)               | Automático (Garbage Collector)           |
| Responsabilidade do programador | Total (alocar e liberar)              | Parcial (alocar apenas)                  |
| Risco de vazamento de memória | Alto, se `free()` não for chamado       | Baixo, GC limpa objetos não utilizados   |
| Controle sobre a memória    | Total                                    | Limitado ao GC                           |
| Complexidade                | Maior (mais propenso a erros)            | Menor (foco na lógica do programa)       |
| Desempenho                 | Alto (depende da habilidade do programador) | Menor em alguns casos (pausas do GC) |
| Indicado para               | Sistemas embarcados, tempo real          | Aplicações empresariais, Android, web    |

---

## Conclusão

O gerenciamento de memória é um aspecto fundamental no desenvolvimento de software. A linguagem C oferece alto controle e desempenho, mas exige atenção rigorosa do programador. Já o Java, com seu GC, facilita a vida do desenvolvedor ao custo de menos controle e, eventualmente, impacto no desempenho.

A escolha da linguagem deve considerar:
- O tipo de aplicação;
- A necessidade de desempenho;
- A complexidade do projeto;
- A experiência da equipe com o gerenciamento de recursos.

---

## Referências

- SEBESTA, Robert W. *Conceitos de Linguagens de Programação*. 10ª ed. Pearson, 2011.
- ORACLE. *Memory Management in Java*. Disponível em: https://docs.oracle.com/javase/specs/
- Cplusplus.com. *malloc - C++ Reference*. Disponível em: https://cplusplus.com/reference/cstdlib/malloc/
- GeeksforGeeks. *Memory Management in C*. Disponível em: https://www.geeksforgeeks.org/memory-management-c/

---

## Autoria
- Aluna: Antonia Fabiana Rodrigues Oliveira
- Disciplina: Linguagens de Programação
- Professor: Bruno Honorato – Universidade Federal do Ceará (UFC).
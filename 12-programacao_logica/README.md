# Desafio 12 – Programação Lógica

Este desafio consiste em modelar um pequeno sistema de genealogia familiar utilizando conceitos da Programação Lógica, com base na sintaxe da linguagem Prolog.

---

## Objetivo
Permitir a inferência de relações familiares como:
- Pai e Mãe
- Irmãos
- Primos
- Avôs e Avós

---

## Linguagem usada
A modelagem foi feita em **Prolog**, utilizando fatos e regras lógicas. Foi utilizado o arquivo `problema_logico.pl`.

---

## Regras implementadas
- `irmao(X, Y)` – X e Y têm os mesmos pais (irmãos completos)
- `primo(X, Y)` – X e Y são filhos de irmãos
- `avo(X, Y)` – X é avô de Y
- `avoh(X, Y)` – X é avó de Y

As regras consideram pai e mãe, e utilizam lógica de inferência com base em fatos definidos no arquivo.

---

## Entrada

>Exemplos de consultas

```prolog
% Quem são os filhos de joao?
pai(joao, X).

% Quem são os irmãos de ana?
irmao(ana, X).

% Quem são os primos de lucas?
primo(lucas, X).

% Quem é o avô de lucas?
avo(X, lucas).

% Quem é a avó de helena?
avoh(X, helena).
```

## Saída

?- pai(joao, X).
X = ana ;
X = pedro.

?- irmao(ana, X).
X = pedro.

?- primo(helena, X).
X = lucas.

---

## Referências

- SEBESTA, Robert W. Conceitos de Linguagens de Programação. 10ª ed. São Paulo: Pearson, 2018.
(Livro-base da disciplina)
- BRATKO, Ivan. Prolog Programming for Artificial Intelligence. 4th Edition. Pearson, 2012.
(Livro clássico sobre Prolog, indicado para aprofundamento)
- SWI-Prolog Official Documentation
(Documentação oficial da ferramenta usada para executar o código)

---

## Autoria
- Aluna: Antonia Fabiana Rodrigues Oliveira
- Disciplina: Linguagens de Programação
- Professor: Bruno Honorato – Universidade Federal do Ceará (UFC)
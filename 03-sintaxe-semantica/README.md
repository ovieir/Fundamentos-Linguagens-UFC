# Desafio 03 – Descrições Sintáticas e Semânticas

## Linguagem fictícia: ComandaLang

## Conceito

A `ComandaLang` é uma linguagem fictícia criada para representar pedidos de restaurante de forma estruturada e simples. Com ela, é possível registrar pedidos por mesa, especificando itens e quantidades. O objetivo é facilitar o entendimento de regras sintáticas e análise léxica usando um exemplo prático e original.

---

## Tokens (Análise Léxica)

| Token           | Significado                             | Exemplo         |
|------------------|------------------------------------------|------------------|
| `pedido`         | Palavra reservada (início do pedido)     | `pedido Mesa1`   |
| `IDENTIFICADOR`  | Nome da mesa ou do cliente               | `Mesa1`, `Mesa2` |
| `:`              | Separador de cabeçalho do pedido         | `:`              |
| `+`              | Adição de item                           | `+ pizza 2`      |
| `ITEM`           | Nome do item do pedido                   | `pizza`, `suco`  |
| `NUM`            | Quantidade de itens                      | `1`, `2`, `3`     |
| `fim`            | Palavra reservada (fim do pedido)        | `fim`            |

---

## Gramática (em pseudocódigo estilo EBNF)

```ebnf
programa     → { pedido }
pedido       → 'pedido' IDENTIFICADOR ':' { item } 'fim'
item         → '+' ITEM NUM
```

## Exemplo 1 – Pedido simples
### Código:
pedido Mesa1:
+ hamburguer 2
+ suco 1
fim

### Análise Léxica:
- [pedido]     → PALAVRA_RESERVADA
- [Mesa1]      → IDENTIFICADOR
- [:]          → SEPARADOR
- [+]          → ADICIONAR
- [hamburguer] → ITEM
- [2]          → NUM
- [+]          → ADICIONAR
- [suco]       → ITEM
- [1]          → NUM
- [fim]        → FIM_PEDIDO

### Análise Sintática:
- pedido → 'pedido' Mesa1 ':' 
-        + hamburguer 2 
-        + suco 1 
-        fim


## Exemplo 2 – Pedido com mais itens
### Código:
- pedido Mesa2:
- + pizza 1
- + refrigerante 2
- + sobremesa 1
- fim

## Análise Léxica:
- [pedido]       → PALAVRA_RESERVADA
- [Mesa2]        → IDENTIFICADOR
- [:]            → SEPARADOR
- [+]            → ADICIONAR
- [pizza]        → ITEM
- [1]            → NUM
- [+]            → ADICIONAR
- [refrigerante] → ITEM
- [2]            → NUM
- [+]            → ADICIONAR
- [sobremesa]    → ITEM
- [1]            → NUM
- [fim]          → FIM_PEDIDO

## Análise Sintática:
- pedido → 'pedido' Mesa2 ':' 
-        + pizza 1 
-        + refrigerante 2 
-        + sobremesa 1 
-        fim

## Considerações Finais
A linguagem ComandaLang foi desenvolvida com o objetivo de exemplificar os conceitos de análise léxica e sintática de maneira criativa e compreensível. Seu formato simula um sistema de pedidos em restaurantes, permitindo que a estrutura da linguagem seja assimilada com facilidade. A gramática simples e os exemplos ilustrativos ajudam a visualizar o funcionamento das regras sintáticas e dos tokens léxicos em um contexto prático.

---

## Referências

- Sebesta, Robert W. *Conceitos de Linguagens de Programação*.
- Notas de aula da disciplina *Linguagens de Programação* – Prof. Bruno de Castro.
- Algumas ideias estruturais foram redigidas com apoio do ChatGPT da OpenAI (sem copiar código pronto).

---

## Autoria

- Aluna: Antonia Fabiana Rodrigues Oliveira
- Disciplina: Linguagens de Programação.
- Professor: Bruno Honorato – Universidade Federal do Ceará (UFC).

---
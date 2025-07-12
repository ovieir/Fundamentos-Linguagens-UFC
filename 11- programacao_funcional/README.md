# Desafio 11 – Programação Funcional

## Objetivo
Este desafio propõe a aplicação do paradigma de programação funcional para resolver um problema simples utilizando **recursão** e **funções de alta ordem**, conforme os conceitos discutidos na disciplina Fundamentos de Linguagens de Programação.

--- 

## Problema
Dada uma lista de pessoas com seus respectivos nomes e idades, deve-se:

1. Filtrar as pessoas com **idade maior ou igual a 18 anos**;
2. Obter os **nomes** dessas pessoas e ordená-los **alfabeticamente**;
3. Calcular o **fatorial da idade** de cada uma das pessoas filtradas utilizando **função recursiva**.

---

## Solução

A solução foi desenvolvida em **Python 3**, utilizando os seguintes recursos da programação funcional:

- `filter()` → para filtrar os maiores de idade;
- `map()` → para mapear dados como nomes e idades;
- `sorted()` → para ordenar os nomes alfabeticamente;
- `lambda` → funções anônimas passadas como argumento;
- Função **recursiva** `fatorial()` → para calcular o fatorial da idade.

---

## Estrutura

Cada arquivo tem uma função clara:
- `funcional_exemplo.py`: contém o código-fonte com a implementação da solução proposta.

---

## Entrada
```python
pessoas = [
    {"nome": "Ana", "idade": 17},
    {"nome": "Carlos", "idade": 20},
    {"nome": "Beatriz", "idade": 22},
    {"nome": "Eduardo", "idade": 16},
    {"nome": "Fernanda", "idade": 19},
]
```

## Saída 

Maiores de idade (ordenados):
- Beatriz
- Carlos
- Fernanda

Fatorial das idades:
Carlos (20 anos): 2432902008176640000
Beatriz (22 anos): 1124000727777607680000
Fernanda (19 anos): 121645100408832000

---

## Referências

- SEBESTA, Robert W. **Conceitos de Linguagens de Programação**. 10ª edição. Pearson, 2011.  
- Documentação oficial do Python: [https://docs.python.org/3/](https://docs.python.org/3/)
- FUNCTOOLS — Higher-order functions and operations on callable objects: [https://docs.python.org/3/library/functools.html](https://docs.python.org/3/library/functools.html)
- W3Schools – Python Functional Programming: [https://www.w3schools.com/python/python_lambda.asp](https://www.w3schools.com/python/python_lambda.asp)

---

## Autoria
- Aluna: Antonia Fabiana Rodrigues Oliveira
- Disciplina: Linguagens de Programação
- Professor: Bruno Honorato – Universidade Federal do Ceará (UFC).

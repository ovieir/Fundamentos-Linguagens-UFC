# Desafio 08 – Programação Orientada a Objetos

## Objetivo

Demonstrar a aplicação dos conceitos de **Programação Orientada a Objetos (POO)**, como herança, polimorfismo e encapsulamento, utilizando a linguagem Java. O exemplo escolhido foi o modelo de veículos, com diferentes tipos: carro, moto e bicicleta.

---

## Linguagem utilizada

- Java

---

## Funcionalidades do código

O programa implementa as seguintes funcionalidades:

- Define uma classe base chamada `Veiculo` com atributos comuns (marca, modelo, ano);
- Cria três subclasses (`Carro`, `Moto`, `Bicicleta`) que herdam de `Veiculo`;
- Cada subclasse sobrescreve o método `mover()` com seu comportamento específico;
- O método `exibirInformacoes()` imprime os dados de cada veículo;
- A execução do programa ocorre por meio da classe `Main`, que instancia objetos das subclasses e exibe seus comportamentos.

---

## Conceitos de POO aplicados

- **Herança**: As subclasses herdam os atributos e métodos da classe `Veiculo`;
- **Polimorfismo**: O método `mover()` é sobrescrito em cada subclasse com comportamento distinto;
- **Encapsulamento**: Uso de construtores e atributos organizados por classe;
- **Classe principal**: `Main` serve como ponto de entrada da aplicação.

---

## Saída esperada:

- --- CARRO ---
- Marca: Toyota
- Modelo: Corolla
- Ano: 2020
- O carro está dirigindo na estrada.

- --- MOTO ---
- Marca: Honda
- Modelo: CG 160
- Ano: 2022
- A moto está acelerando.

- --- BICICLETA ---
- Marca: Caloi
- Modelo: Explorer
- Ano: 2021
- A bicicleta está pedalando.

---

## Referências
- SEBESTA, Robert W. Conceitos de Linguagens de Programação. 10ª ed. Pearson, 2018.
- Notas de aula da disciplina de Linguagens de Programação – UFC.

---

## Autoria
- Aluna: Antonia Fabiana Rodrigues Oliveira
- Disciplina: Linguagens de Programação
- Professor: Bruno Honorato – Universidade Federal do Ceará (UFC).

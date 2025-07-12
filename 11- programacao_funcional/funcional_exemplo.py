from functools import reduce

# Lista de pessoas com nome e idade
pessoas = [
    {"nome": "Ana", "idade": 17},
    {"nome": "Carlos", "idade": 20},
    {"nome": "Beatriz", "idade": 22},
    {"nome": "Eduardo", "idade": 16},
    {"nome": "Fernanda", "idade": 19},
]

# Função recursiva: fatorial

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


# Funções de alta ordem
# 1. Filtra apenas maiores de idade
maiores = list(filter(lambda p: p["idade"] >= 18, pessoas))

# 2. Mapeia nomes dos maiores
nomes_maiores = list(map(lambda p: p["nome"], maiores))

# 3. Ordena alfabeticamente os nomes
nomes_ordenados = sorted(nomes_maiores)

# 4. Calcula o fatorial da idade de cada maior de idade
fatoriais_idades = list(map(lambda p: (p["nome"], p["idade"], fatorial(p["idade"])), maiores))


# Saídas
print("Maiores de idade (ordenados):")
for nome in nomes_ordenados:
    print("-", nome)

print("\nFatorial das idades:")
for nome, idade, fat in fatoriais_idades:
    print(f"{nome} ({idade} anos): {fat}")

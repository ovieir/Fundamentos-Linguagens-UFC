# Exemplo em Python – Tipagem Dinâmica e Forte
x = 10
y = 3.5
print("Soma:", x + y)  # OK: int e float são compatíveis

x = "texto"
# print(x + y)  # Erro em tempo de execução: não soma string com float

#Tipos são definidos em tempo de execução. Operações inválidas, como somar string com número, são bloqueadas pelo interpretador.
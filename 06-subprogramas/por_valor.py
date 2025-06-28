def dobrar(numero):
# Esta função tenta dobrar o valor do parâmetro recebido.
    numero = numero * 2
    print("Dentro da função: número =", numero)

# código principal
    valor = 10
    print("Antes da função: valor =", valor)
    dobrar(valor)
    print("Depois da função: valor =", valor)
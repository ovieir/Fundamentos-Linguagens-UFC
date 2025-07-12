# Importa a biblioteca 'requests' para fazer requisições HTTP
import requests

# Importa o BeautifulSoup da biblioteca 'bs4' para fazer o parsing (análise) do HTML
from bs4 import BeautifulSoup

# Função que coleta os livros a partir de uma URL
def coletar_livros(url):
    # Faz uma requisição GET para a URL
    resposta = requests.get(url)
    
    # Verifica se a resposta da requisição foi bem-sucedida (código 200)
    if resposta.status_code != 200:
        print("Erro ao acessar o site")  # Mostra mensagem de erro se falhar
        return  # Encerra a função

    # Cria um objeto BeautifulSoup com o conteúdo HTML da página
    soup = BeautifulSoup(resposta.text, 'html.parser')

    # Seleciona todos os elementos de livros com a classe 'product_pod'
    livros = soup.select('article.product_pod')

    # Exibe uma mensagem informando o início da listagem
    print("Lista de livros encontrados:\n")

    # Percorre cada livro encontrado
    for livro in livros:
        # Obtém o título do livro acessando o atributo 'title' da tag <a> dentro do <h3>
        titulo = livro.h3.a['title']

        # Obtém o preço do livro selecionando o elemento com a classe 'price_color'
        preco = livro.select_one('.price_color').text

        # Exibe o título e o preço no terminal
        print(f"Título: {titulo}\nPreço: {preco}\n{'-'*40}")

# Bloco principal do programa (só é executado se o script for chamado diretamente)
if __name__ == "__main__":
    # Define a URL da página que será analisada
    url = 'https://books.toscrape.com/catalogue/page-1.html'

    # Chama a função para coletar os dados da página
    coletar_livros(url)

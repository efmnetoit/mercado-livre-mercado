import urllib.request
import bs4 as bs

def pesquisar(produto, menor):
    tratamento = input("Quer ser chamado de pai ou mãe?").lower()

    #produto = "microondas"
    url = "https://lista.mercadolivre.com.br/{}".format(produto)
    print("Acessando site...")
    pagina = urllib.request.urlopen(url)  # Pegando código da página
    codigo_pagina = bs.BeautifulSoup(pagina, features="html.parser")
    print("Pesquisando produtos...")

    itens = codigo_pagina.find_all('span', attrs={'class': 'price__fraction'})
    links = codigo_pagina.find_all('a', attrs={'class': 'item__info-title'})

    #menor = 300
    posicao = 0
    volta = 0

    for i in itens:
        valor = float(i.text.strip().replace('.', ""))
        if valor < menor:
            menor = valor
            posicao = volta
        volta = volta + 1
    print("Se armou!!! Vai pagar ", menor, "pila no", produto, "hein", tratamento, "!")
    print(links[posicao].get('href'))

#Se quiser rodar no mesmo arquivo
#if __name__ = "__main__":
#    pesquisar("microondas", 300)

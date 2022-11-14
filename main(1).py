import Grafo as gf
import random


def leitor(nome: str):

    with open(nome) as arquivos:
        return arquivos.read().splitlines()


def main():
    grafo = gf.GRAFO()

    nomes = leitor("Users.txt")

    n_veretices = int(input("numero de vertices: "))
    n_arestas = int(input("numero de arestas: "))
    #derecionado = input("é derecionado?: ")

    for i in range(n_veretices):
        grafo.adiciona_vertice(random.choice(nomes))

    grafo.adiciona_aresta(random.choice(grafo.nome_vertice()),  random.choice(grafo.nome_vertice()), random.randint(1, 100))

    for i in range(n_arestas):
        vertice = grafo.nome_vertice()
        grau = grafo.list_grau()
        grafo.adiciona_aresta(random.choice(random.choices(vertice, weights=grau)), random.choice(vertice), random.randint(1, 100))

    grafo.imprime_lista_adjacencias()


if __name__ == '__main__':
    main()

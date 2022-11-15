import Grafo as gf
import random


def leitor(nome: str):
    with open(nome) as arquivos:
        return arquivos.read().splitlines()


def criar_grafo_aleatorio(n_ver, n_arestas, direcionado):
    grafo = gf.GRAFO(direcionado)
    nomes = leitor("Users.txt")

    while grafo.numero_vertices() != n_ver:
        grafo.adiciona_vertice(random.choice(nomes))

    lista_vertices = grafo.nome_vertice()
    grafo.adiciona_aresta(random.choice(grafo.nome_vertice()),
                          random.choice(grafo.nome_vertice()),
                          random.randint(1, 100))

    nu_arestas = n_arestas

    if direcionado == False:
        nu_arestas = nu_arestas * 2

    if type(direcionado) == bool:
        while grafo.numero_arrestas() < nu_arestas:
            lista_graus = grafo.list_grau()
            nome_aleatorio_1 = random.choice(random.choices(lista_vertices, weights=lista_graus))
            nome_aleatorio_2 = random.choice(lista_vertices)
            n_rand = random.randint(1, 100)
            if direcionado == True:
                if not grafo.tem_aresta(nome_aleatorio_1, nome_aleatorio_2):
                    grafo.adiciona_aresta(nome_aleatorio_1,
                                          nome_aleatorio_2,
                                          n_rand)

            else:
                if not grafo.tem_aresta(nome_aleatorio_1, nome_aleatorio_2):
                    grafo.adiciona_aresta(nome_aleatorio_1,
                                          nome_aleatorio_2,
                                          n_rand)

                    grafo.adiciona_aresta(nome_aleatorio_2,
                                          nome_aleatorio_1,
                                          n_rand)

        return grafo
    else:
        print("Direcionado é bool")


def DAG(grafo):
    if grafo.direcionado == True:
        print("oi")
    else:
        print("Parametro invalido")


def main():
    grafo = criar_grafo_aleatorio(100, 100, True)
    DAG(grafo)


if __name__ == '__main__':
    main()

import copy

import Grafo as gf
import random


def leitor(nome: str):
    with open(nome) as arquivos:
        return arquivos.read().splitlines()


class Grafo_Random:
    def __init__(self, n_ver, n_arestas, direcionado):
        self.n_ver = n_ver
        self.n_arestas = n_arestas
        self.direcionado = direcionado
        self.grafo = gf.GRAFO()
        self.criar_grafo_aleatorio()

    def criar_grafo_aleatorio(self):
        nomes = leitor("Users.txt")

        while self.grafo.numero_vertices() != self.n_ver:
            self.grafo.adiciona_vertice(random.choice(nomes))

        lista_vertices = self.grafo.nome_vertice()
        self.grafo.adiciona_aresta(random.choice(self.grafo.nome_vertice()),
                                   random.choice(self.grafo.nome_vertice()),
                                   random.randint(1, 100))

        nu_arestas = self.n_arestas

        if not self.direcionado:
            nu_arestas = nu_arestas * 2

        if type(self.direcionado) == bool:
            while self.grafo.numero_arrestas() < nu_arestas:
                lista_graus = self.grafo.list_grau()
                nome_aleatorio_1 = random.choice(random.choices(lista_vertices, weights=lista_graus))
                nome_aleatorio_2 = random.choice(lista_vertices)
                n_rand = random.randint(1, 100)
                if self.direcionado:
                    if not self.grafo.tem_aresta(nome_aleatorio_1, nome_aleatorio_2):
                        self.grafo.adiciona_aresta(nome_aleatorio_1,
                                                   nome_aleatorio_2,
                                                   n_rand)

                else:
                    if not self.grafo.tem_aresta(nome_aleatorio_1, nome_aleatorio_2):
                        self.grafo.adiciona_aresta_n_direcionado(nome_aleatorio_1,
                                                                 nome_aleatorio_2,
                                                                 n_rand)

        else:
            print("Direcionado é bool")


    def Kahn_Algorithm(self):
        if self.direcionado:
            lista = []
            total = list(self.grafo.grafo.keys())
            grau_zerado = [0] * (self.grafo.numero_vertices())
            for vertice in total:
                grau_entrada = self.grafo.grau_entrada(vertice)
                numero_de_vertices = grau_entrada
                if numero_de_vertices == 0:
                    lista.append(vertice)
                    self.grafo.remove_vertice(vertice)

            sorted_list = []
            while lista:
                vertice_lista = lista.pop()
                sorted_list.append(vertice_lista)
                for vertice_vizinho in self.grafo.grafo.get(vertice_lista, []):
                    grau_zerado[vertice_vizinho] -= 1
                    if grau_zerado[vertice_vizinho] == 0:
                        lista.append(vertice_vizinho)

            if len(sorted_list) != len(grau_zerado):
                return True
            else:
                return print(sorted_list)
        else:
            return print("grafo não é direcionado")

    def dag(self):
        while self.Kahn_Algorithm():
            self.grafo.remove_aresta_vertice(random.choice(self.grafo.maior_grau_sem_n()))

    def transformador_conexo(self):
        if self.direcionado:
            return print("grafo é direcionado")
        else:
            for vertice in self.grafo.grafo:
                if self.grafo.grau(vertice) == 0:
                    self.grafo.adiciona_aresta_n_direcionado(random.choice(self.grafo.nome_vertice()),
                                               random.choice(self.grafo.nome_vertice()),
                                               random.randint(0, 100))




def main():
    grafo_random = Grafo_Random(100, 150, True)
    grafo_random_copy = copy.deepcopy(grafo_random)
    grafo_random_copy.dag()


if __name__ == '__main__':
    main()

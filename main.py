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

        if self.direcionado == False:
            nu_arestas = nu_arestas * 2

        if type(self.direcionado) == bool:
            while self.grafo.numero_arrestas() < nu_arestas:
                lista_graus = self.grafo.list_grau()
                nome_aleatorio_1 = random.choice(random.choices(lista_vertices, weights=lista_graus))
                nome_aleatorio_2 = random.choice(lista_vertices)
                n_rand = random.randint(1, 100)
                if self.direcionado == True:
                    if not self.grafo.tem_aresta(nome_aleatorio_1, nome_aleatorio_2):
                        self.grafo.adiciona_aresta(nome_aleatorio_1,
                                              nome_aleatorio_2,
                                              n_rand)

                else:
                    if not self.grafo.tem_aresta(nome_aleatorio_1, nome_aleatorio_2):
                        self.grafo.adiciona_aresta(nome_aleatorio_1,
                                              nome_aleatorio_2,
                                              n_rand)

                        self.grafo.adiciona_aresta(nome_aleatorio_2,
                                              nome_aleatorio_1,
                                              n_rand)

        else:
            print("Direcionado é bool")

    def transposto(self, vertice1, vertice2, grafo):
        if grafo.tem_aresta(vertice1, vertice2):
            peso_ = grafo.peso(vertice1, vertice2)
            grafo.remove_aresta(vertice1, vertice2)
            grafo.adiciona_aresta(vertice2, vertice1, peso_)
        else:
            return False

    def transpor_grafo(self):
        for value in self.grafo.grafo.values():
            print(value)

    def dag(self, grafo):
        if grafo.direcionado == True:
            print("oi")
        else:
            print("Parametro invalido")


def main():
    grafo_ramdom = Grafo_Random(50, 50, True)
    grafo_ramdom.transpor_grafo()


if __name__ == '__main__':
    main()

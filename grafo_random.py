import grafo as gf
import numpy as np
import random
import matplotlib.pyplot as plt


class Grafo_Random:
    def __init__(self, n_ver, n_arestas, direcionado):
        self.n_ver = n_ver
        self.n_arestas = n_arestas
        self.direcionado = direcionado
        self.grafo = gf.GRAFO(direcionado)
        self.criar_grafo_aleatorio()
        self.gerar_lista_nomes()

    def gerar_lista_nomes(self):
        dic_nomes = {}
        txt = open("Users.txt")
        nomes = txt.read().splitlines()
        for i in range(self.n_ver):
            dic_nomes[i] = random.choice(nomes)
        self.dic_nomes = dic_nomes

    def gerar_matrix_random(self, n_vertices, n_arestas):
        p1 = n_arestas / (n_vertices ** 2 * 1.001)
        p0 = 1 - p1
        matrix = np.random.choice([0, 1], size=(n_vertices, n_vertices), p=[p0, p1])
        return matrix

    def matrix_para_grafo_ndirecinado(self, n_vertices, n_arestas):
        matrix = self.gerar_matrix_random(n_vertices, n_arestas * 2)  # duas vezes mais por ser ndirecional

        for i in range(len(matrix)):  # 0 ao numero de vertices
            self.grafo.adiciona_vertice(i)

        for v1 in range(len(matrix)): # triangulo
            for v2 in range(v1):
                if matrix[v1][v2] == 1:
                    w = np.random.randint(100)
                    self.grafo.adiciona_aresta(v1, v2, w) # duas vezes mais por ser ndirecional
                    self.grafo.adiciona_aresta(v2, v1, w)

    def matrix_para_grafo_direcinado(self, n_vertices, n_arestas):
        matrix = self.gerar_matrix_random(n_vertices, n_arestas)

        for i in range(len(matrix)):
            self.grafo.adiciona_vertice(i)

        for v1 in range(len(matrix)):
            for v2 in range(len(matrix)):
                if matrix[v1][v2] == 1:
                    w = np.random.randint(100)
                    self.grafo.adiciona_aresta(v1, v2, w)

    def criar_grafo_aleatorio(self):
        if type(self.direcionado) == bool:
            self.matrix_para_grafo_direcinado(self.n_ver, self.n_arestas)
            if not self.direcionado:
                self.matrix_para_grafo_ndirecinado(self.n_ver, self.n_arestas)
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
        for chave, valores in self.grafo.grafo.items():
            if len(valores) > 0:
                for valor in valores:
                    peso = self.grafo.peso(chave, valor[0])
                    self.grafo.remove_aresta(chave, valor[0])
                    self.grafo.adiciona_aresta(valor[0], chave, peso)
        print(self.grafo.imprime_lista_adjacencias())

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
            self.grafo.remove_aresta_vertice(random.choice(self.grafo.maior_grau()))

    def pajek(self):
        grafoDotNet = open("grafo.net", "w")
        n = 1
        grafoDotNet.write("*vertices" + " " + str(self.grafo.numero_vertices()) + "\n")
        for vertice in self.grafo.grafo:
            grafoDotNet.write(str(n) + " " + self.dic_nomes[vertice] + "\n")
            n += 1
        vertice_atual = 1

        if self.direcionado:
            grafoDotNet.write("*arcs \n")
        else:
            grafoDotNet.write("*edges \n")

        for vertice in self.grafo.grafo:
            vertice_1 = vertice
            vertice_teste = 1
            for vertice in self.grafo.grafo:
                if self.grafo.tem_aresta(vertice_1, vertice) == True:
                    grafoDotNet.write(str(vertice_atual) + " " + str(vertice_teste) + "\n")
                vertice_teste += 1
            vertice_atual += 1
        grafoDotNet.close()

    def lerpajek(self):
        new_grafo = gf.GRAFO(self.direcionado)
        txt = open("grafo.net")
        lines = txt.read().splitlines()
        acc = 0
        dic_names = {}
        for line in lines:
            if acc != 0 and acc <= self.grafo.numero_vertices():
                id_, name = line.split()
                new_grafo.adiciona_vertice(name)
                dic_names[id_] = name
            elif acc >= self.grafo.numero_vertices() + 3:
                name1, name2 = line.split()
                new_grafo.adiciona_aresta(dic_names[name1], dic_names[name2], 0)
            acc += 1
        txt.close()
        return new_grafo

    def transformador_conexo(self):
        if self.direcionado:
            print("grafo é direcionado")
        else:
            for vertice in self.grafo.grafo:
                while self.grafo.grau(vertice) == 0:
                    self.grafo.adiciona_aresta_n_direcionado(vertice,
                                                             random.choice(self.grafo.nome_vertice()),
                                                             random.randint(0, 100))

    def plot_grau_hist(self):
        plt.hist(self.grafo.list_grau())
        plt.ylabel("n vertices")
        plt.xlabel("Grau")
        return plt.show()

    def plot_caminho_min_hist(self):
        plt.hist(self.grafo.create_all_Dijkstra())
        plt.ylabel("n vertices")
        plt.xlabel("Grau")
        return plt.show()

    def numero_comp_ndirecionado(self, grafo=None):
        if grafo:
            if self.direcionado == False:
                vertices = grafo.nome_vertice()
                visitados = []
                acc = 0
                for i in vertices:
                    cond = True
                    for i1 in grafo.busca_largura(i):
                        if i1 in visitados:
                            cond = False
                        else:
                            visitados.append(i1)
                    if cond == True:
                        acc += 1
                return acc
            else:
                return "Precisa ser não direcional"
        else:
            if self.direcionado == False:
                vertices = self.grafo.nome_vertice()
                visitados = []
                acc = 0
                for i in vertices:
                    cond = True
                    for i1 in self.grafo.busca_largura(i):
                        if i1 in visitados:
                            cond = False
                        else:
                            visitados.append(i1)
                    if cond == True:
                        acc += 1
                return acc
            else:
                return "Precisa ser não direcional"

    def arvore_minima_ndirecionado(self):
        #if self.numero_comp_ndirecionado() == 1:
        grafo1 = gf.GRAFO(False)
        lista_caminho = self.grafo.busca_profundidade(0)
        for i in lista_caminho:
            grafo1.adiciona_vertice(i)
        for i in range(len(lista_caminho)-1):
            grafo1.adiciona_aresta(lista_caminho[i], lista_caminho[i+1], 0)
            grafo1.adiciona_aresta(lista_caminho[i + 1], lista_caminho[i], 0)
        self.grafo = grafo1
        #else:
        #    print("Grafo não é conexo ou direcional")
        #    return

    def imprime_lista_adjacencias(self):
        aresta = ""
        for key, value in self.grafo.grafo.items():
            for i in value:
                aresta += "["+self.dic_nomes[i[0]]+f", {i[1]}]" + " -> "
            print(f"{self.dic_nomes[key]} : {aresta}")
            aresta = ""


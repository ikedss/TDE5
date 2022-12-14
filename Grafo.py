import math


class GRAFO:
    def __init__(self):
        self.grafo = {}

    def adiciona_vertice(self, nome_vertice):
        if nome_vertice in self.grafo:
            return False
        else:
            self.grafo[nome_vertice] = []

    def adiciona_aresta(self, vertice1, vertice2, peso):
        if self.tem_aresta(vertice1, vertice2):
            return False
        else:
            self.grafo[vertice1].append([vertice2, peso])

    def adiciona_aresta_n_direcionado(self, vertice1, vertice2, peso):
        if self.tem_aresta(vertice1, vertice2):
            return False
        else:
            self.grafo[vertice1].append([vertice2, peso])
            self.grafo[vertice2].append([vertice1, peso])

    def remove_aresta(self, vertice1, vertice2):
        nova_lista = []
        if self.tem_aresta(vertice1, vertice2):
            for i in self.grafo[vertice1]:
                if i[0] != vertice2:
                    nova_lista.append(i)
            self.grafo[vertice1] = nova_lista
        else:
            print(f"Aresta entre {vertice1} -> {vertice2} não existe")

    def remove_aresta_vertice(self, vertice):
        if vertice not in self.grafo:
            print(f"Vertice {vertice} não existe")
        else:
            for chave, valores in self.grafo.items():
                for valor in valores:
                    if valor[0] == vertice:
                        self.remove_aresta(chave, vertice)

    def remove_vertice(self, vertice):
        if vertice not in self.grafo:
            print(f"Vertice {vertice} não existe")
        else:
            del self.grafo[vertice]
            for chave, valores in self.grafo.items():
                for valor in valores:
                    if valor[0] == vertice:
                        self.remove_aresta(chave, vertice)

    def tem_aresta(self, vertice1, vertice2):
        if vertice1 not in self.grafo or vertice2 not in self.grafo:
            return False
        for i in self.grafo[vertice1]:
            if i[0] == vertice2:
                return True
        return False

    def peso(self, vertice1, vertice2):
        if self.tem_aresta(vertice1, vertice2):
            for i in self.grafo[vertice1]:
                if i[0] == vertice2:
                    return i[1]
        return f"Aresta entre {vertice1} -> {vertice2} não existe"

    def verificador_euleriano(self):
        eulerian = True
        for vertice in self.grafo.keys():
            if not self.grau(vertice) % 2:
                eulerian = False
        return eulerian

    def imprime_lista_adjacencias(self):
        aresta = ""
        for key, value in self.grafo.items():
            for i in value:
                aresta += str(i) + " -> "
            print(f"{key} : {aresta}")
            aresta = ""

    def numero_vertices(self):
        return len(self.grafo.keys())

    def numero_arrestas(self):
        acc = 0
        for value in self.grafo.values():
            for i in value:
                acc += 1
        return acc

    def nome_vertice(self):
        return list(self.grafo.keys())

    def grau(self, vertice):
        acc = 0
        if vertice in self.grafo:
            for i in self.grafo.keys():
                if vertice in [x[0] for x in self.grafo[i]] and i != vertice:
                    acc += 1
            return len(self.grafo[vertice]) + acc
        return f"Vertice {vertice} não existe"

    def maior_grau(self):
        listagraumax = []
        for vertice in self.grafo:
            numero_de_vertices = self.grau(vertice)
            listagraumax.append([numero_de_vertices, vertice])
        return sorted(listagraumax, key=lambda x: x[0], reverse=True)[:1]

    def maior_grau_sem_n(self):
        lista = []
        for i in self.maior_grau():
            for j in i:
                if j in range(self.numero_arrestas()):
                    del j
                else:
                    lista.append(j)
        return lista

    def list_grau(self):
        lista = []
        for vertice in self.grafo.keys():
            lista.append(self.grau(vertice))
        return lista

    def grau_entrada(self, keys):
        listaentrada = []
        for vertice in self.grafo:
            for adjacencias in self.grafo[vertice]:
                if adjacencias[0] == keys:
                    listaentrada.append(vertice)
        return len(listaentrada)

    def grau_saida(self):
        listaentrada = {}
        for vertice in self.grafo.keys():
            listaentrada[vertice] = len(self.grafo[vertice])
        listaentrada = sorted(listaentrada.items(), key=lambda x: x[1], reverse=True)
        return listaentrada[:1]

    def grau_entrada_max(self):
        listaentradamax = []
        for vertice in self.grafo:
            numero_de_vertices = self.grau_entrada(vertice)
            listaentradamax.append([numero_de_vertices, vertice])
        return sorted(listaentradamax, key=lambda x: x[0], reverse=True)[:1]

    def x_arestas(self, vertice, D):
        lista_vertices = []
        visitados = []
        fila = []
        fila.append(vertice)
        acc = 0
        while acc != D:
            acc += 1
            if fila[0] not in visitados:
                visitados.append(fila[0])
                for x in self.grafo[fila[0]][::-1]:
                    if x[0] not in lista_vertices:
                        lista_vertices.append(x[0])
                    if x[0] not in visitados:
                        fila.append(x[0])
            del fila[0]
        return lista_vertices

    def Dijkstra(self, start, end):
        dic_ = {key: math.inf for key in self.grafo if key != start}
        dic_[start] = 0
        visited = [start]
        acc = 0
        direcion = []
        best_direcion = [end]
        while end not in visited:
            for key, value in self.grafo[visited[acc]]:
                if key in visited:
                    continue
                new_distance = value + dic_[visited[acc]]
                if dic_[key] > new_distance:
                    direcion.append([visited[acc], key])
                    dic_[key] = new_distance
                visited.append(key)
            acc += 1
        end_word = end
        for i in direcion[::-1]:
            if end_word == i[1]:
                best_direcion.append(i[0])
                end_word = i[0]
        return dic_[end], best_direcion[::-1]

    def Dijkstra_clear(self, start):
        dic_ = {key: math.inf for key in self.grafo if key != start}
        dic_[start] = 0
        visited = [start]
        acc = 0
        direcion = []
        while len(visited) != acc or acc == 0:
            for key, value in self.grafo[visited[acc]]:
                if key in visited:
                    continue
                new_distance = value + dic_[visited[acc]]
                if dic_[key] > new_distance:
                    direcion.append([visited[acc], key])
                    dic_[key] = new_distance
                visited.append(key)
            acc += 1
        return dic_

    def create_all_Dijkstra(self):
        one_key = list(self.grafo.keys())[0]

        init_dic = self.Dijkstra_clear(one_key)
        while math.inf in init_dic.values():
            for key, values in init_dic.items():
                if values == math.inf:
                    init_dic_other = self.Dijkstra_clear(key)
                    for key1, value1 in init_dic_other.items():
                        if init_dic[key1] != init_dic_other[key1] and value1 != math.inf:
                            init_dic[key1] = value1
                    print(len([i for i in init_dic.values() if i == math.inf]))
        print(max(init_dic.values()))

    def create_all_Dijkstra1(self):
        acc = 0
        for i in self.grafo.keys():
            init_dic = self.Dijkstra_clear(i)
            if max(init_dic.values()) > acc:
                acc = max(init_dic.values())
        return acc

    def busca_profundidade(self, vertice, fim):
        visitados = []
        pilha = []
        pilha.append(vertice)
        while fim not in visitados:
            s = pilha.pop()
            if s not in visitados:
                visitados.append(s)
                for x in self.grafo[s][::-1]:
                    if x[0] not in visitados:
                        pilha.append(x[0])
        return visitados

    def busca_largura(self, vertice, fim):
        visitados = []
        fila = []
        fila.append(vertice)
        while fim not in visitados:
            if fila[0] not in visitados:
                visitados.append(fila[0])
                for x in self.grafo[fila[0]][::-1]:
                    if x[0] not in visitados:
                        fila.append(x[0])
            del fila[0]
        return visitados

    def pajek(self):
        grafoDotNet = open("grafo.net", "w")
        n = 1
        grafoDotNet.write("*vertices" + " " + str(self.grafo.numero_vertices()) + "\n")
        for vertice in self.grafo.grafo:
            grafoDotNet.write(str(n) + " " + vertice + "\n")
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
                if self.grafo.tem_aresta(vertice_1, vertice):
                    grafoDotNet.write(str(vertice_atual) + " " + str(vertice_teste) + "\n")
                vertice_teste += 1
            vertice_atual += 1
        grafoDotNet.close()

    def lerpajek(self):
        nome_arestas = []
        id_arestas = []
        lst_conec = []
        lst_conec1 = []
        conec = True
        with open("grafo.net") as f:
            arquivo = f.readlines()
            for linha in arquivo:
                data = linha.split()
                if data[0] != "*vertices" and data[0] != "*arcs" and data[0] != "*edges":
                    if conec:
                        print(data[1])
                        self.grafo.adiciona_vertice(data[1])
                        nome_arestas.append(data[1])
                        id_arestas.append(data[0])
                    else:
                        lst_conec.append(data[0])
                        lst_conec1.append(data[1])

                if data[0] == "*arcs" and "*edges":
                    conec = False
                    direcionado = data[0]

        lst_vertices = list(zip(id_arestas, nome_arestas))
        lst_arestas = list(zip(lst_conec, lst_conec1))

        lst_verticeA = []
        lst_verticeB = []

        for arestas in lst_arestas:
            vertice_atual = arestas[0]
            vertice_conectado = arestas[1]
            for vertice in lst_vertices:
                if vertice[0] == vertice_atual:
                    lst_verticeA.append(vertice[1])
                if vertice[0] == vertice_conectado:
                    lst_verticeB.append(vertice[1])

        lst_ligada = list(zip(lst_verticeA, lst_verticeB))

        if direcionado == "*arcs":
            for item in lst_ligada:
                self.grafo.adiciona_aresta(item[0], item[1], 0)
        else:
            for item in lst_ligada:
                self.grafo.adiciona_aresta(item[0], item[1], 0)
                self.grafo.adiciona_aresta(item[1], item[0], 0)

        self.grafo.imprime_lista_adjacencias()
        f.close()

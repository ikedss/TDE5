
import grafo_testes as gt
import timeit
import grafo as gf

class SCC:
    def __init__(self, grafo):
        self.grafo = grafo
        self.dic_visitados = self.criar_dicionario_vistados()
        self.pilha = []

    def criar_dicionario_vistados(self):
        dic_visitados = {}
        for i in self.grafo.grafo.keys():
            dic_visitados[i] = False
        return dic_visitados

    def transpor_grafo(self):
        new_grafo_transposto = gf.GRAFO(self.grafo.direcionado)
        for i in self.grafo.grafo.keys():
            new_grafo_transposto.adiciona_vertice(i)
        for chave in self.grafo.grafo.keys():
            valores = self.grafo.grafo[chave]
            if len(valores) > 0:
                for valor in valores:
                    peso = self.grafo.peso(chave, valor[0])
                    new_grafo_transposto.adiciona_aresta(valor[0], chave, peso)
        return new_grafo_transposto

    def visitar(self, v):
        self.dic_visitados[v] = True

    def DFSUtil(self, v, visited, grafo):
        visited[v] = True
        print(v)
        for i in grafo[v]:
            if visited[i[0]] == False:
                self.DFSUtil(i[0], visited, grafo)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.grafo.grafo[v]:
            if visited[i[0]] == False:
                self.fillOrder(i[0], visited, stack)
        stack = stack.append(v)

    def printSCCs(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)

        visited = self.dic_visitados
        # Fill vertices in stack according to their finishing
        # times
        for i in self.grafo.grafo.keys():
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

            # Create a reversed graph
        gf = self.transpor_grafo()

        # Mark all the vertices as not visited (For second DFS)
        visited = self.criar_dicionario_vistados()

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                self.DFSUtil(i, visited, gf.grafo)
                print("")

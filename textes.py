def transpor_grafo(grafo):
    for chave, valores in grafo.grafo.items():
        if len(valores) > 0:
            for valor in valores:
                peso = grafo.peso(chave, valor[0])
                grafo.remove_aresta(chave, valor[0])
                grafo.adiciona_aresta(valor[0], chave, peso)

def dfs_iterative(start, grafo):
    stack, path = [start], []
    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue

        path.append(vertex)
        for neighbor in grafo[vertex]:
            stack.append(neighbor[0])
    return path


def dfs_little(v ,lista_vertices, grafo):
    lista_vertices[v] = True
    print(v)
    for i in grafo[v]:
        if lista_vertices[i[0]] == False:
            dfs_iterative(i[0], lista_vertices, grafo)

def fillOrder(v,lista_vertices, stack, grafo):
    lista_vertices[v] = True
    for i in grafo[v]:
        if lista_vertices[i[0]] == False:
            fillOrder(i[0], lista_vertices, stack, grafo)
    stack = stack.append(v)



# dic_vertices = {}
#
# def scc(grafo):
#     stack = []
#
#     for i in grafo.grafo.keys():
#         dic_vertices[i] = False
#
#     for i in grafo.grafo.keys():
#         if dic_vertices[i] == False:
#             fillOrder(i, dic_vertices, stack, grafo.grafo)
#
#     transpor_grafo(grafo)
#
#     for i in grafo.grafo.keys():
#         dic_vertices[i] = False
#
#     while stack:
#         i = stack.pop()
#         if dic_vertices[i] == False:
#             dfs_iterative(i, dic_vertices, grafo.grafo)
#             print("")




def scc(grafo):
    pilha = []
    visitados = []
    #proximo = list(grafo.grafo.keys())[0]
    proximo = "C"
    while len(pilha) != grafo.numero_vertices():
        existe = False
        ini = timeit.default_timer()
        resu = dfs_iterative(proximo, grafo.grafo)
        fin = timeit.default_timer()
        tempo = fin - ini
        print("resultado : ", resu)
        print("proximo : ", proximo)
        for i in resu:
            if i not in visitados:
                visitados.append(i)
                existe = True
        if existe:
            pilha.append(resu[::-1][0])
            proximo = resu[::-1][1]
        else:
            if len(resu) == 1:
                pilha.append(proximo)
            proximo = [i for i in grafo.grafo.keys() if i not in pilha][0]

        print("pilha : ", pilha)
        print("visitados : ", visitados)
        print("#--------------------------------------------#")
    print(pilha)
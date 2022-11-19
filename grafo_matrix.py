import numpy as np
import grafo as gf

def gerar_matrix_random(n_vertices, n_arestas):
    p1 = n_arestas / (n_vertices ** 2)
    p0 = 1 - p1
    matrix = np.random.choice([0, 1], size=(n_vertices, n_vertices), p=[p0, p1])
    return matrix

def matrix_para_grafo_ndirecinado(n_vertices, n_arestas):
    matrix = gerar_matrix_random(n_vertices, n_arestas * 2)

    grafo = gf.GRAFO()
    for i in range(len(matrix)):
        grafo.adiciona_vertice(i)

    for v1 in range(len(matrix)):
        for v2 in range(v1):
            if matrix[v1][v2] == 1:
                w = np.random.randint(100)
                grafo.adiciona_aresta(v1, v2, w)
                grafo.adiciona_aresta(v2, v1, w)

    print(grafo.numero_arrestas())
    print(matrix.sum())

def matrix_para_grafo_direcinado(n_vertices, n_arestas):
    matrix = gerar_matrix_random(n_vertices, n_arestas)

    grafo = gf.GRAFO()
    for i in range(len(matrix)):
        grafo.adiciona_vertice(i)

    for v1 in range(len(matrix)):
        for v2 in range(len(matrix)):
            if matrix[v1][v2] == 1:
                w = np.random.randint(100)
                grafo.adiciona_aresta(v1, v2, w)

    print(grafo.numero_arrestas())
    print(matrix.sum())

def main():
    matrix_para_grafo_ndirecinado(10000, 15000)
    matrix_para_grafo_direcinado(10000, 15000)

if __name__ == "__main__":
    main()

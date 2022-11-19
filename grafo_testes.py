import grafo

def grafo_teste1():
    grafo_text = grafo.GRAFO()
    grafo_text.adiciona_vertice("A")
    grafo_text.adiciona_vertice("B")
    grafo_text.adiciona_vertice("C")
    grafo_text.adiciona_vertice("D")
    grafo_text.adiciona_vertice("E")
    grafo_text.adiciona_vertice("F")
    grafo_text.adiciona_vertice("G")
    grafo_text.adiciona_vertice("H")

    grafo_text.adiciona_aresta("A", "B", 1)
    grafo_text.adiciona_aresta("B", "E", 1)
    grafo_text.adiciona_aresta("B", "F", 1)
    grafo_text.adiciona_aresta("B", "C", 1)
    grafo_text.adiciona_aresta("C", "D", 1)
    grafo_text.adiciona_aresta("C", "G", 1)
    grafo_text.adiciona_aresta("D", "C", 1)
    grafo_text.adiciona_aresta("D", "H", 1)
    grafo_text.adiciona_aresta("E", "A", 1)
    grafo_text.adiciona_aresta("E", "F", 1)
    grafo_text.adiciona_aresta("F", "G", 1)
    grafo_text.adiciona_aresta("G", "F", 1)
    grafo_text.adiciona_aresta("G", "H", 1)
    return grafo_text

def grafo_teste2():
    grafo_text = grafo.GRAFO(False)
    grafo_text.adiciona_vertice("0")
    grafo_text.adiciona_vertice("1")
    grafo_text.adiciona_vertice("2")
    grafo_text.adiciona_vertice("3")
    grafo_text.adiciona_vertice("4")
    grafo_text.adiciona_vertice("5")

    grafo_text.adiciona_aresta("0", "1", 1)
    grafo_text.adiciona_aresta("0", "2", 1)
    grafo_text.adiciona_aresta("1", "2", 1)
    grafo_text.adiciona_aresta("4", "5", 1)
    return grafo_text
import grafo

def grafo_texte1():
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
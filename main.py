import grafo_random as gr
import scc
import copy
import time
import grafo_testes as gt

def main():
    # ----------------------------------------------------- EX 1 eu#
    # ini = time.time()
    grafo_random = gr.Grafo_Random(100, 300, False)
    # fin = time.time()
    # print("tempo = ", fin - ini)
    # print("numero arrestas = ", grafo_random.grafo.numero_arrestas())
    # print("numero vertices = ", grafo_random.grafo.numero_vertices())
    # ----------------------------------------------------- EX 2 #
    # grafo_random.pajek()
    # ----------------------------------------------------- EX 3 eu#
    # new_grafo = grafo_random.lerpajek()
    # new_grafo.imprime_lista_adjacencias()
    # ----------------------------------------------------- EX 4 eu#
    # print(grafo_random.numero_comp_ndirecionado())
    # ----------------------------------------------------- EX 5 eu#
    # grafo1 = gt.grafo_teste1()
    # scc1 = scc.SCC(grafo1)
    # scc1.printSCCs()
    # scc1 = scc.SCC(grafo_random.grafo)
    # scc1.printSCCs()
    # ----------------------------------------------------- EX 6 #
    # grafo_random_copy = copy.deepcopy(grafo_random)
    # grafo_random_copy.dag()
    # ----------------------------------------------------- EX 7 #
    # grafo_random.plot_grau_hist()
    # ----------------------------------------------------- EX 8 eu#
    # grafo_random.plot_caminho_min_hist()
    # ----------------------------------------------------- EX 11 #
    # grafo_random.transformador_conexo()
    # ----------------------------------------------------- EX 12 eu#
    # grafo_random.arvore_minima_ndirecionado()
    # grafo_random.imprime_lista_adjacencias()

    # print(grafo_random.grafo.numero_arrestas())
    # -----------------------------------------------------#


if __name__ == "__main__":
    main()


import random
import networkx as nx
import matplotlib.pyplot as plt

estados = {
    "CDMX": 500,
    "Jalisco": 800,
    "Nuevo León": 700,
    "Querétaro": 600,
    "Yucatán": 1000,
    "Chiapas": 900,
    "Sonora": 1200
}


relaciones_estados = [
    ("CDMX", "Jalisco", 800),
    ("CDMX", "Querétaro", 600),
    ("CDMX", "Sonora", 1200),
    ("Jalisco", "Nuevo León", 700),
    ("Nuevo León", "Querétaro", 600),
    ("Querétaro", "Yucatán", 1000),
    ("Yucatán", "Chiapas", 900),
    ("Chiapas", "Sonora", 1200)
]

def recorrer_sin_repetir():
    grafo = nx.Graph()
    grafo.add_weighted_edges_from(relaciones_estados)

    camino = list(nx.algorithms.approximation.traveling_salesman_problem(grafo))

    costo_total = sum(grafo[u][v]['weight'] for u, v in zip(camino, camino[1:]))

    print("Recorrido sin repetir estados:")
    for estado in camino:
        print(f"Ir a {estado}")
    print(f"\nCosto total del recorrido: ${costo_total}")

    
    nx.draw(grafo, with_labels=True, node_size=1500, node_color='lightblue', font_size=10, font_weight='bold', width=2)
    plt.title("Grafo de recorrido sin repetir estados")
    plt.show()

def recorrer_con_repetir():
    grafo = nx.Graph()
    grafo.add_weighted_edges_from(relaciones_estados)

    estados_visitados = []
    total_costo = 0

    estado_actual = random.choice(list(estados.keys()))
    estados_visitados.append(estado_actual)
    estados_restantes = set(estados.keys()) - set([estado_actual])

    for _ in range(6):
        estado_siguiente = random.choice(list(grafo.neighbors(estado_actual)))
        estados_visitados.append(estado_siguiente)
        total_costo += grafo[estado_actual][estado_siguiente]['weight']
        estado_actual = estado_siguiente

    print("\nRecorrido con posibilidad de repetir estados:")
    for estado in estados_visitados:
        print(f"Ir a {estado}")
    print(f"\nCosto total del recorrido: ${total_costo}")

    nx.draw(grafo, with_labels=True, node_size=1500, node_color='lightblue', font_size=10, font_weight='bold', width=2)
    plt.title("Grafo de recorrido con posibilidad de repetir estados")
    plt.show()

recorrer_sin_repetir()
recorrer_con_repetir()


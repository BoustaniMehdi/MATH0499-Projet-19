"""
Ce fichier contient le code gérant la logique de simulation.

Auteurs: Boustani Mehdi - Tingue Lucynda
Date: 7 décembre 2023
Projet: 19
"""

import networkx as nx
import matplotlib.pyplot as plt
from agent import Agent
import random
from network import Graph
import matplotlib.animation as animation

# Variables
min_degree = 3 # Degré minimum des noeuds ( > 1)
frames = 20 # Nombre de frames pour l'animation (idéal : [10, 20])

# Fonction principale de la simulation
def run_simulation(num_communities,num_agents):
    
    num_infected_agent = random.randint(1, min(3, num_agents)) # Nombre aléatoire d'agent infecté au départ
    
    graph = Graph(num_agents, num_communities, min_degree) # Graph principal
    
    # Création du graph selon le nombre de communauté
    graph.create_communities()
    
    # Interconnexité dans chaque communautés
    graph.connect_local_nodes()
    
    # Connexité globale du graph G
    graph.connect_communities()
    
    # 1 agent = 1 noeud
    agents = {node: Agent(id=node) for node in graph.G.nodes}
    
    # Selection d'agents aléatoirement dans l'intervalle [1, num_infected_agent]
    infected_agents = random.sample(list(agents.values()), num_infected_agent)
    
    # Infection des agents selectionnés aléatoirement
    for agent in infected_agents:
        agent.infect()
    
    # Stockage de l'état inital du graph pour l'afficher au début de l'animation
    initial_state = [agents[node].status for node in graph.G.nodes]
    
    # Stockage des instantanés (état variables des agents)
    snapshots = [initial_state]
    
    # Boucle principale de la simulation
    for _ in range(frames):
        # Sélection aléatoire des voisins des agents sains et si ils sont infectés, ils le deviennent aussi
        for agent in agents.values():
            if agent.status == "healthy":
                neighbors = list(graph.G.neighbors(agent.id))
                # Nombre de recontres par l'agent
                encounters = random.randint(1, len(neighbors))
                # Voisins rencontré par l'agent
                neighbors_to_meet = random.sample(neighbors, encounters)
                # Infection si on rencontre un infecté
                for neighbor in neighbors_to_meet:
                    if agents[neighbor].status == "infected":
                        agent.infect()
                        break # Si l'agent est infecté, on peut sortir de la boucle
                
            agent.update()
                
        # Création de l'instantané de l'état actuel du graph
        snapshot = [agents[node].status for node in graph.G.nodes]
        # On concatène cette liste à l'ensemble des instantanés
        snapshots.append(snapshot)

    # Animation du graph avec les instantanés
    animate_graph(snapshots,graph)

# Fonction d'animation du graph utilisant la bibliothèque matplotlib.animation
def animate_graph(snapshots,graph):
    fig, ax = plt.subplots()
    position = nx.spring_layout(graph.G)
    node_colors = [graph.state_colors.get(status, "#01FE01") for status in snapshots[0]]
    nx.draw(graph.G, position, with_labels=False, node_color=node_colors, node_size=10)
    
    # Mise à jour des couleurs des noeuds selon les instantanés
    def update(frames):
        node_colors = [graph.state_colors.get(status, "#01FE01") for status in snapshots[frames]]
        ax.clear() # On évite les surimpression du graph
        nx.draw(graph.G, position, with_labels=False, node_color=node_colors, node_size=10)
        
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=150, repeat=False)
    plt.show()
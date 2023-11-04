import networkx as nx
import random
import matplotlib.pyplot as plt
from agent import Agent

class Graph:
    def __init__(self, num_nodes, num_communities, min_degree):
        self.G = nx.Graph()
        self.num_nodes = num_nodes
        self.min_degree = min_degree
        self.num_communities = num_communities
        self.community_size = num_nodes // num_communities
        self.communities = []
        self.state_colors = {
            "healthy": "#01FE01",
            "infected": "#FF0000",
            "cured": "#00A9FF"
        }

    def create_communities(self):
        for i in range(self.num_communities):
            community = list(range(i * self.community_size, (i + 1) * self.community_size))
            self.communities.append(community)
            self.G.add_nodes_from(community)

    def connect_local_nodes(self):
        for community in self.communities:
            for node in community:
                for _ in range(self.min_degree):
                    target = random.choice(community)
                    # On évite les boucles
                    if target != node:
                        self.G.add_edge(node, target)

    def connect_communities(self):
        for i in range(self.num_communities):
            current_community = self.communities[i]
            next_community = self.communities[(i + 1) % self.num_communities]
            other_community = self.communities[(i + 2) % self.num_communities]

            for _ in range(self.num_communities):
                # Communautés voisines
                source_node = random.choice(current_community)
                target_node = random.choice(next_community)
                if(source_node != target_node):
                    self.G.add_edge(source_node, target_node)
                # Autre communauté 
                source_node = random.choice(current_community)
                target_node = random.choice(other_community)
                if(source_node != target_node):
                    self.G.add_edge(source_node, target_node)

    def init_graph(self, graph_state):
        
        position = nx.spring_layout(self.G)
        # Attribution des couleurs aux nœuds en fonction de l'état de leurs agents
        node_colors = [self.state_colors.get(status, "#01FE01") for status in graph_state]
        
        nx.draw(self.G, position, with_labels=False, node_color=node_colors, node_size=10)
        
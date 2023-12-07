"""
Ce fichier contient la fonction principale du projet de simulation de propagation de maladie.

Auteurs: Boustani Mehdi - Tingue Lucynda
Date: 7 décembre 2023
Projet: 19
"""

import networkx as nx
import matplotlib.pyplot as plt
from simulation import run_simulation

def main():
    min_agents = 1
    max_agents = 700
    min_communities = 1
    max_communities = 10
    
    # Demande à l'utilisateur combien d'agents et de communautés il souhaite créer
    num_agents = get_input(f"Combien d'agents voulez-vous créer ([{min_agents}, {max_agents}]) ?  ", min_agents, max_agents)
    
    if num_agents < max_communities:
        max_communities = num_agents
    
    num_communities = get_input(f"Combien de communautés souhaitez-vous créer ([{min_communities}, {max_communities}]) ? ", min_communities, max_communities)

            
    print(f"Vous avez choisi {num_agents} agent(s) et {num_communities} communauté(s).")
    run_simulation(num_communities,num_agents)
    
def get_input(message, min, max):
    valid = False
    while not valid:
        try:
            value = int(input(message))
            if min <= value <= max:
                valid = True
            else:
                if value < min:
                    print("C'est trop petit ! Veuillez entrer une valeur plus grande: ")
                else:
                    print("C'est trop grand ! Veuillez entrer une valeur plus petite: ")
        except ValueError:
            print("Veuillez entrer un nombre valide: ")
    
    return value


if __name__ == "__main__":
        
    main()
   
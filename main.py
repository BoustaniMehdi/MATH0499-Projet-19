"""
Ce fichier contient la fonction principale du projet de simulation de propagation de maladie.

Auteurs: Boustani Mehdi - Tingue Lucynda
Date: 7 octobre 2023
Projet: 19
"""

import networkx as nx
import matplotlib.pyplot as plt
from simulation import run_simulation
from agent import Agent

def main():
    # Demande à l'utilisateur combien d'agents et de communautés il souhaite créer
    num_agents = int(input("Combien d'agents (sommets) voulez-vous créer ? "))
    num_communities = int(input("Combien de communautés souhaitez-vous créer ? "))

    # Vérifie si les valeurs entrées sont dans les limites acceptables
    if num_agents > 700 or num_communities > 10:
        print("C'est trop grand ! Veuillez entrer une valeur plus petite.")
    else:
        print(f"Vous avez choisi {num_agents} agent. et {num_communities} communautés.")
        
    run_simulation(num_communities,num_agents)

if __name__ == "__main__":
        
    main()
   
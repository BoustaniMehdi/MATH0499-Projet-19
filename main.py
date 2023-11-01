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
    run_simulation()

if __name__ == "__main__":

# Demande à l'utilisateur combien d'agents et de communautés il souhaite créer
agent = Agent()
communities = create_communities()
agent = int(input("Combien d'agents (sommets) voulez-vous créer ? "))
communities = int(input("Combien de communautés souhaitez-vous créer ? "))

# Vérifie si les valeurs entrées sont dans les limites acceptables
if agent > 700 or communities > 10:
    print("C'est trop grand ! Veuillez entrer une valeur plus petite.")
else:
    print(f"Vous avez choisi {agent} agent. et {communities} communautés.")
    # Vous pouvez ajouter le code pour travailler avec ces valeurs ici.
main()
   
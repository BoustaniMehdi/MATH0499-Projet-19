"""
Ce fichier contient la définition de la classe Agent.

Auteurs: Boustani Mehdi - Tingue Lucynda
Date: 7 octobre 2023
Projet: 19
"""

class Agent:
    def __init__(self, id, state="healthy"):
        self.id = id
        self.status = state
        self.days_infected = 0
    
    def infect(self):
        if (self.status == "healthy"):
            self.status = "infected"
            self.days_infected = 0
            
    def heal(self):
        if self.status == "infected" and self.days_infected >= 30:   
            self.status = "healthy"
            self.days_infected = 0
    
    def update(self):
        if self.status == "infected":   
            self.days_infected += 1
            self.heal()
    
    def __str__(self):
        return f"Agent {self.id} ; Status : {self.status} ; Days infected : {self.days_infected}"
        
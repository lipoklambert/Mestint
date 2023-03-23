import numpy as np
from node import Node

# Próba-hiba módszer
def trial_error(problem):
    # kezdő állapot
    state = Node(problem.initial)

    while True: 
        # Ha a probléma megoldva, akkor leállítjuk a végtelen ciklust
        if problem.goal_test(state.state):
            print("Got it")
            return state
        # Az alkalmazható operátorok segítségével 
        # gyártsuk le az összes lehetséges utódot
        successors = state.expand(problem)

        # Ha nincs új állapot (utód)
        if len(successors)==0:
            return "Usolvable"
        
        # Random választunk egy újat a legyártott utódok közül
        state = successors[np.random.randint(0,len(successors))]
        print(state.state)
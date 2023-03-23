from problem import Problem
from search import trial_error
from search_szelessegi_melysegi import breadth_first_tree_search
from search_szelessegi_melysegi import depth_first_graph_search
from heur import sort_by_heur
from search_astar import astar_search

class NQueens(Problem):
    """Egy állapotot n elemu tombkent abrazolunk ahol a c-edik bejegyzesben szereplo r erteke azt jelenti,hogy a c oszlopban, az r sorban van egy kiralyno,
     a -1 ertek pedig azt, hogy a c-edik oszlop meg nem lett kitoltve.
     balrol jobbra toltjuk az oszlopokat."""
    def __init__(self, N):
        super().__init__(tuple([-1]*N))
        self.N = N

    def actions(self, state):
        #bal szelso ures oszlopban probalja ki az osszes nem utkozo sort
        if state[-1] != -1:
            return [] #minden oszlop kitoltve
        else:
            col = state.index(-1)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]
        
    def result(self, state, row):
        #helyezze a kovetkezo kiralynot a megadott sorba
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)
    
    def conflicted(self, state, row, col):
        # egy kiralyno elhelyezese (sor, oszlop) utkozik?
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))
    
    def conflict(self, row1, col1, row2, col2):
        #osszeutkozesbe kerulne ket kiralyno elhelyezese (sor1, oszlop1) es (sor2, oszlop2)?
        return (row1 == row2 or # ugyanabban a sorban
                col1 == col2 or # ugyanbban az oszlopban
                row1 - col1 == row2 - col2 or
                row1 + col1 == row2 + col2)
    
    def goal_test(self, state):
        #ellenorizze hogy minden oszlpo megtelt e es nics utkozes
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))
    
np4 = NQueens(4)
print(np4.initial, np4.goal)
print("-"*30)
print(trial_error(np4))
print("-"*30)
print(depth_first_graph_search(np4))
print("-"*30)
print(breadth_first_tree_search(np4))
print("-"*30)
print(astar_search(np4, sort_by_heur))
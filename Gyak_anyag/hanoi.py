from problem import Problem
from collections import namedtuple
from search import trial_error
from search_szelessegi_melysegi import breadth_first_tree_search
from search_szelessegi_melysegi import depth_first_graph_search
State=namedtuple("State", ["disk","char"])

class Hanoi(Problem):
    def __init__(self, n):
        # n darab korongunk van
        self.size = n

        # "1" * n : Kezdő állapot, Hány darab korong van az 1-es...
        # "3" * n : Cél állapot, Hány darab korong van az 3-as...
        super().__init__("1" * n, "3" * n)

    def actions(self, state):
        """Operátorok definiálása"""
        acts = []

        # Nézzük meg az egyes rúdak állapotát
        f1 = state.find("1")
        f2 = state.find("2")
        f3 = state.find("3")
        
        # Ha az 1. rúd nem üres és tartalma kisebb mint ami
        # a 2. rúdon van vagy a 2. rúd üres, akkor
        # az 1. rúdról átrakhatunk a 2. rúdra
        if -1 < f1 and (f1 < f2 or f2 == -1):
            acts.append(State(f1, "2"))

        if -1 < f1 and (f1 < f3 or f3 == -1):
            acts.append(State(f1, "3"))

        if -1 < f2 and (f2 < f1 or f1 == -1):
            acts.append(State(f2, "1"))

        if -1 < f2 and (f2 < f3 or f3 == -1):
            acts.append(State(f2, "3"))

        if -1 < f3 and (f3 < f1 or f1 == -1):
            acts.append(State(f3, "1"))

        if -1 < f3 and (f3 < f2 or f2 == -1):
            acts.append(State(f3, "2"))

        return acts

    def result(self, state, action):
        # disk = korong, char = rúd
        disk, char = action

        # Előtte és utána lévő korongok helyeinek összefűzése
        return state[0:disk] + char + state[disk + 1:]
    

Student = namedtuple('Student', ['name', 'age', 'DOB'])
S = Student('Nandini', '19', '2541997')
print("Index is :", S[0])

h = Hanoi(3)
h.size, h.initial, h.goal
print(trial_error(h).solution())
print("--"*30)
print(breadth_first_tree_search(h).solution())
print("--"*30)
print(depth_first_graph_search(h).solution())
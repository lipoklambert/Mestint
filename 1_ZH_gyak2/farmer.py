from problem import Problem
from node import Node

def is_valid(f, g, w, l) -> bool:
    return (f == w and g != l) or \
        (f == l and w != g) or \
        (f == g) or \
        (w != g and g != l)


class Farmer(Problem):

    def actions(self, state):
        f, g, w, l = state
        # state - 4 elemű lista, melyben az elemek
        # 1 és 0, attól függően hogy átkelt-e már az ember (vagy állat/káposzta)
        acts = []
        # act - 2 elemű lista, melynek az első eleme a célszemély indexe a state listában
        # második eleme pedig a célállapot

        if is_valid(1, g, w, l):
            acts.append([0, 1])

        if is_valid(f, 1, w, l):
            acts.append([1, 1])

        if is_valid(f, g, 1, l):
            acts.append([2, 1])

        if is_valid(f, g, w, 1):
            acts.append([3, 1])

        if f == 1 and is_valid(0, g, w, l):
            acts.append([0, 0])

        return acts

    def result(self, state, action):
        # note: valószínű meg lehetett volna oldani a meglévő state list módosításával
        #       uj lista létrehozása nélkül, de minden kínom volt szóval így maradt nem akartam a pythonnal 1v1ezni

        # felbontjuk a state listát az elemeinkre
        f, g, w, l = state
        # felbontjuk az az action listát a célszemély indexére és célallapotra
        user, celallapot = action
        # csinálok egy uj listát az utazók állapotából
        new = [f, g, w, l]
        # módosítjuk a célszemély állapotát
        new[user] = celallapot
        # visszaadjuk az utazók módosítás utáni állapotát 
        return new

    def goal_test(self, state):
        return all(user == 1 for user in state)
    """def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
    def actions(self, state):
        farmer, goat, wolf, cabbage = state
        possible_actions = []
        if farmer == 0:
            # farmer can only take goat, wolf, or cabbage when he is on the left side
            if goat == 0 and cabbage == 0:
                possible_actions.append("take goat")
            if wolf == 0 and goat == 0:
                possible_actions.append("take wolf")
            if cabbage == 0:
                possible_actions.append("take cabbage")
        else:
            # farmer can only take goat, wolf, or cabbage when he is on the right side
            if goat == 1 and cabbage == 1:
                possible_actions.append("take goat")
            if wolf == 1 and goat == 1:
                possible_actions.append("take wolf")
            if cabbage == 1:
                possible_actions.append("take cabbage")
        possible_actions.append("cross river")
        return possible_actions
    
    def result(self, state, action):
        farmer, goat, wolf, cabbage = state
        new_state = list(state)
        if action == "take goat":
            new_state[1] = 1 - goat
            new_state[0] = 1 - farmer
        elif action == "take wolf":
            new_state[2] = 1 - wolf
            new_state[0] = 1 - farmer
        elif action == "take cabbage":
            new_state[3] = 1 - cabbage
            new_state[0] = 1 - farmer
        else:
            new_state[0] = 1 - farmer
        # check if the new state is valid
        if (new_state[1] == new_state[3] and new_state[0] != new_state[1]) or \
                (new_state[2] == new_state[1] and new_state[0] != new_state[2]):
            return tuple(new_state)
        return None"""
    

    """def actions(self, state):
        actions = []
        for i in range(1, 5):
            if state[0] == state[i]:
                new_state = list(state)
                new_state[0] = 1 - new_state[0]
                new_state[i] = 1 - new_state[i]
                if self.is_valid_state(new_state):
                    actions.append(i)
        return actions

    def result(self, state, action):
        new_state = list(state)
        new_state[0] = 1 - new_state[0]
        new_state[action] = 1 - new_state[action]
        return tuple(new_state)

    def is_valid_state(self, state):
        if state[1] == state[2] and state[0] != state[1]:
            return False
        if state[2] == state[3] and state[0] != state[2]:
            return False
        return True"""



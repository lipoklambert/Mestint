import random

from problem import Problem
from node import Node
from collections import deque

def breadth_first_tree_search(problem):

    frontier = deque([Node(problem.initial)])

    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None

class Digits(Problem):

    def __init__(self):
        self.wrong_numbers = [(6,6,6),(6,6,7)]
        self.s4 = 0

        # Complete the implementation of initial function by calling
        # the parent constructor and initialize the initial state and set of goal states
        # Write your code below this line!
        super().__init__((5,7,6),[(7,7,7)])

        # Write your code above this line! Delete the 'pass' keyword!

    def actions(self, state):
        s1, s2, s3 = state
        acts = []

        # Complete the remaining part of the action function
        # Write your code below this line!
        if (s1 + 1, s2, s3) not in self.wrong_numbers and self.s4 != 1 and s1 + 1 <= 9:
            acts.append('s1_plus')
        if (s1, s2+1, s3) not in self.wrong_numbers and self.s4 != 2 and s2 + 1 <= 9:
            acts.append('s2_plus')
        if (s1, s2, s3+1) not in self.wrong_numbers and self.s4 != 3 and s3 + 1 <= 9:
            acts.append('s3_plus')
        if (s1-1, s2, s3) not in self.wrong_numbers and self.s4 != 1 and s1 - 1 >= 0:
            acts.append('s1_minus')
        if (s1, s2-1, s3) not in self.wrong_numbers and self.s4 != 2 and s2 - 1 >= 0:
            acts.append('s2_minus')
        if (s1, s2, s3-1) not in self.wrong_numbers and self.s4 != 3 and s2 - 1 >= 0:
            acts.append('s3_minus')
        # Write your code above this line!
        return acts

    def result(self, state, action):
        s1, s2, s3 = state
        # Complete the implementation of result function
        # Write your code below this line!
        if action == 's1_plus':
            self.s4 = 1
            return (s1 + 1, s2, s3)
        if action == 's2_plus':
            self.s4 = 2
            return (s1 , s2+1, s3)
        if action == 's3_plus':
            self.s4 = 3
            return (s1 , s2, s3+1)
        if action == 's1_minus':
            self.s4 = 1
            return (s1-1 , s2, s3)
        if action == 's2_minus':
            self.s4 = 2
            return (s1 , s2-1, s3)
        if action == 's3_minus':
            self.s4 = 3
            return (s1 , s2, s3-1)
        # Write your code above this line!


if __name__ == '__main__':
    d = Digits()
    print(d.initial, d.goal)
    print(d.actions(d.initial))
    print(d.result(d.initial, 's2_minus'))
    print(breadth_first_tree_search(d))
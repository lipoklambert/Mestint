from node import Node
from collections import deque

def breadth_first_tree_search(problem):
    #kezdő állapot kiolvasasa es FIFO sorba helyezese
    frontier = deque([Node(problem.initial)])

    # Amíg ne ertuk el a hatart
    while frontier:
        # legszelsobb elem kiemelese
        node = frontier.popleft()

        # ha cel allapotban vagyunk akkor vege
        if problem.goal_test(node.state):
            return node
        
        #a kiemelt elembol az osszes uj allapot legyartasa az operatorok segitsegevel
        frontier.extend(node.expand(problem))
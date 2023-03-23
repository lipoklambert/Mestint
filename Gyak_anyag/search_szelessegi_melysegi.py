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


def depth_first_graph_search(problem):
    #kezdo elem verembe helyezese
    frontier = [(Node(problem.initial))]
    #halmaz deklaralasa a mar bejart elemekhez
    explored = set()

    #amig tudunk melyebbre menni
    while frontier:
        # legfelso elem kiemelese a verembol
        node = frontier.pop()

        # ha cel allapotban vagyunk, vege
        if problem.goal_test(node.state):
            return node

        #allapot feljegyzese hogy tudjuk hogy mar jartunk itt
        explored.add(node.state)

        # verem bovitese a meg be nem jart elemekkel
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)    
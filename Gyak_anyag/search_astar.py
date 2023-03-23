from node import Node

def astar_search(problem, f=None):
    """
    az a* algoritmus olyan a-algoritmusfajta, mely garantalja az optimalis megoldas eloa
    h*(n) : az n-bol valamely celcsucsba jutas optimalis koltsege
    g*(n) : a startcsucsbol n-be jutas optimalis koltsegee
    f*(n) = g*(n)+h*(n) : ...
    """
    return best_first_graph_search(problem, f)

def best_first_graph_search(problem, f):
    #kezdo allapot letrehozasa
    node = Node(problem.initial)
    #prioritasos sor letrehozasa
    frontier = []
    #kezdo allapot felvetele a prioritasos sorba
    frontier.append(node)
    # halmaz letrehozasa a mar megvizsaglt elemekhez
    explored = set()

    #amig elemet nem talalunk
    while frontier:
        #elem kivetele a verem tetejerol
        node = frontier.pop()
        # ha cel allapotban vagyunk akkor kesz
        if problem.goal_test(node.state):
            return node
        #feldolgozott elemek bovitese
        explored.add(node.state)
        #operatorral legyartott gyermek elemek bejarasa
        for child in node.expand(problem):
            # ha meg nem dolgoztuk fel
            if child.state not in explored and child not in frontier:
                frontier.append(child)
        # rendezzuk a listat a heurisztikanak megfeleloen
        frontier = f(frontier)
        print(node.state)
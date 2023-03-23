# ez nem egy optimalis heurisztika!
def sort_by_heur(items):
    #valasszuk mindig a leheto legnagyobb indexu sort
    return sorted(items, key = lambda x: sum(x.state))
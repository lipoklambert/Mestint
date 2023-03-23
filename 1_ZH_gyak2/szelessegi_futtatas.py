from szelessegi import breadth_first_tree_search
from farmer import Farmer

f = Farmer((0,0,0,0), (1,1,1,1))
print(breadth_first_tree_search(f).solution())
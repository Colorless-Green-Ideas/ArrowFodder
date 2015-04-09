import networkx as nx
import matplotlib.pyplot as plt

class alt(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return self.name == other.name

def arr(x,z):
    "x prefered or indifferent to z"
    pass


# My_list = [alt("Code"), alt("Eat"), alt("Do Laundry"), alt("Shave")]

DG=nx.DiGraph()

# This is a Strong ordering there is no indifference
DG.add_edges_from([(alt("Code"), alt("Eat")), (alt("Eat"), alt("Do Laundry")),
    (alt("Do Laundry"), alt("Shave"))])
nx.draw_networkx(DG)
plt.show()
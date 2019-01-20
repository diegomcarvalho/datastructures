from collections import defaultdict, deque
from .LinkedList import LinkedList

class BagStack(list):
    def __init__(self) -> None:
        list(self)
        return
    def add(self, data) -> None:
        self.append(data)
        return
    def take(self) -> object:
        return self.pop()

class BagQueue(deque):
    def __init__(self) -> None:
        deque(self)
        return
    def add(self, data):
        self.appendleft(data)
        return
    def take(self) -> object:
        return self.pop()


class Graph:
    """ Implements a representation of a Graph 

        G = (V,E)

        where V is a node set and E a edge set.

        A node can be any Python data type and edges are created
        by add_edge method.

    """

    def __init__(self) -> None:
        self.VEset = defaultdict(LinkedList)
        self.Ew = dict()

    def __str__(self) -> str:
        lstr = list()
        for i, v in self.VEset.items():
            for j in v:
                w = self.Ew[(i,j)]
                lstr.append(f"{i} - {w} -> {j}\n")
        return ''.join(lstr)

    def add_direct_edge(self, i, j, w=1) -> None:
        """ insets into E an edge from i to j
        """
        self.VEset[i].append(j)
        self.Ew[(i,j)] = w
        return

    def add_edge(self, i, j, w=1) -> None:
        """ insets into E both edges from i to j and from j to i
        """
        self.VEset[i].append(j)
        self.VEset[j].append(i)
        self.Ew[(i,j)] = w
        self.Ew[(j,i)] = w
        return

    def is_edge(self, i, j):
        """ returns True if (i,j) belongs to E
        """ 
        if j in self.VEset[i]:
            return True
        return False

    def _whatever_first_search(self, bag, node, func_visit=None) -> list:
        visited = set()
        node_order_list = list()

        bag.add(node)
        while bag:
            v = bag.take()
            if v not in visited:
                visited.add(v)
                node_order_list.append(v)
                if func_visit: func_visit(v)
                for i in self.VEset[v]:
                        bag.add(i)

        return node_order_list

    def breadth_first_search(self, node, func_visit=None) -> list:
        if node not in self.VEset:
            raise KeyError
        bag = BagQueue()
        return self._whatever_first_search(bag, node, func_visit)

    def depth_first_search(self, node, func_visit=None) -> list:
        if node not in self.VEset:
            raise KeyError
        bag = BagStack()
        return self._whatever_first_search(bag, node, func_visit)

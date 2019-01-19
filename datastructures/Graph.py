from collections import defaultdict, deque
from .LinkedList import LinkedList

class Graph:

    def __init__(self) -> None:
        self.VEset = defaultdict(LinkedList)

    def __str__(self) -> str:
        lstr = list()
        for k, v in self.VEset.items():
            for j in v:
                lstr.append(f"{k} -> {j} ")
        lstr.append("\n")
        return ''.join(lstr)

    def add_direct_edge(self, i, j) -> None:
        self.VEset[i].append(j)
        return

    def add_edge(self, i, j) -> None:
        self.VEset[i].append(j)
        self.VEset[j].append(i)
        return

    def is_edge(self, i, j):
        if j in self.VEset[i]:
            return True
        return False


    def breadth_first_search(self, node, func_visit=None) -> list:
        visited = set()
        queue = deque()
        bfs = list()
        visited.add(node)
        bfs.append(node)
        if func_visit:
            func_visit(node)
        queue.appendleft(node)
        while queue:
            v = queue.pop()
            for i in self.VEset[v]:
                if i not in visited:
                    visited.add(i)
                    bfs.append(i)
                    if func_visit:
                        func_visit(i)
                    queue.appendleft(i)
        return bfs

    def depth_first_search(self, node, func_visit=None) -> list:
        visited = set()
        stack = deque()
        dfs = list()
        visited.add(node)
        dfs.append(node)
        if func_visit:
            func_visit(node)
        stack.append(node)
        while stack:
            v = stack.pop()
            for i in self.VEset[v]:
                if i not in visited:
                    visited.add(i)
                    dfs.append(i)
                    if func_visit:
                        func_visit(i)
                    stack.append(i)
        return dfs
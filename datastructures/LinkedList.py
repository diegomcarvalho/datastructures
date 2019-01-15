class LinkedListNode:

    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next
        return

    #def __repr__(self):
    #    return repr(self.data)

    def __str__(self) -> str:
        return str(self.data)

class LinkedListIterator:
    def __init__(self, source) -> None:
        self.node = source.head
        return

    def __iter__(self):
        return self

    def __next__(self):
        if self.node == None:
            raise StopIteration
        data = self.node.data
        self.node = self.node.next
        return data

class LinkedList:
    """LinkedList - Double Linked List

    This class implements a double linked list in Python.

    Attributes:
        head
        tail
        len
    """

    def __init__(self, inter=None) -> None:
        """Initializes head, tail and len.
        
        Parameters:

        inter: inter
            Used to initialize the List with a List, Set, Dict, etc.
        """
        self.head = None
        self.tail = None
        self.len = 0

        if inter == None:
            return
        for i in inter:
            self.insert(i)       
        return

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return repr(nodes)

    def __str__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr.data)
            curr = curr.next
        return str(nodes)

    def __len__(self):
        return self.len

    def __iter__(self):
        return LinkedListIterator(self)

    def __eq__(self, l2):
        curr1 = self.head
        curr2 = l2.head

        while curr1 and curr2:
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        if curr1 or curr2:
            return False

        return True

    def __getitem__(self, key):
        if key >= self.len:
            raise KeyError

        curr = self.head

        while curr and key:
            curr = curr.next
            key -= 1

        if not curr:
            raise KeyError

        return curr.data

    def __setitem__(self, key, value):
        if key >= self.len:
            raise KeyError

        curr = self.head

        while curr and key:
            curr = curr.next
            key -= 1

        if not curr:
            raise KeyError
            
        curr.data = value

        return

    def __contains__(self, item):
        return self.find(item)

    def is_empty(self):
        return self.tail == None

    def insert(self, data):
        # inserts data in the begining of the list
        # Time complexity: O(1)
        new_head = LinkedListNode(data, next=self.head)

        if self.is_empty():
            self.tail = new_head
        else:
            self.head.prev = new_head

        self.head = new_head

        self.len += 1

        return

    def append(self, data):
        new_tail = LinkedListNode(data, prev=self.tail)

        if self.is_empty():
            self.head = new_tail
        else:
            self.tail.next = new_tail

        self.tail = new_tail

        self.len += 1

        return

    def find(self, key):
        for i in self:
            if key == i:
                return True
        return False

    def find_node(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return curr
            curr = curr.next
        return None

    def find_previous_node(self, key):
        curr = self.head
        while curr.next:
            if curr.next.data == key:
                return curr
            curr = curr.next
        return None

    def remove_elem(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev

        node.prev = None
        node.next = None
        del node

        self.len -=  1

        return

    def remove(self, key):
        node = self.find_node(key)

        if not node:
            return

        self.remove_elem(node)

        return

    def delete(self):
        self.remove_elem(self.head)

        self.len -= 1

        return

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        self.tail = self.head
        prev_node = None
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        self.head = prev_node.prev

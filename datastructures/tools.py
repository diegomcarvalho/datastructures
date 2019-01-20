from .LinkedList import LinkedListNode, LinkedList

def remove_dups( ls: LinkedList ) -> None:
    item_list = set()

    curr = ls.head
    while curr:
        if curr.data in item_list:
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        else:
            item_list.add(curr.data)
        curr = curr.next
    return

def print_k_to_the_last(head, k):
    if head == None:
        return 0
    index = print_k_to_the_last(head.next, k) + 1
    if index == k:
        print(f'{k}th to the last node is {head.data}')
    return index

def sum_list(l1, l2):
    curr1 = l1.head
    curr2 = l2.head
    carry = 0
    result = LinkedList()

    while curr1:
        if not curr2:
            break
        val = curr1.data + curr2.data + carry
        carry = 1 if val >= 10 else 0
        result.insert(val%10)
        curr1 = curr1.next
        curr2 = curr2.next

    return result
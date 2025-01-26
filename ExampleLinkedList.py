class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.nextNode = None


class LinkedList:
    def __init__(self, head) -> None:
        self.head = head

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.val} -> ")
            current = current.nextNode
        print("Nonde")


head = Node(123)
ll = LinkedList(head=head)


node2 = Node(1234)
head.nextNode = node2


node3 = Node(34)
node2.nextNode = node3


ll.print_list()

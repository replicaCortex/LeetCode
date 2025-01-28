# @leet start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head
        list = []
        tmp = ListNode()

        if current != None:
            list.append(current.val)
            current = current.next

        for i in range(len(list), 0, -1):
            tmp.val(list[i])
            tmp.next

        print(tmp)


# @leet end

head_ = [1, 2, 4, 5]
head = ListNode(head_[0])
current = head

for i in range(1, len(head_)):
    current.next = ListNode(val=head_[i])
    current = head.next

head.printList()

# @leet start
# Definition for singly-linked list.


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def printList(self):
#     current = self
#     while current:
#         print(current.val, end=" -> ")
#         current = current.next
#     print("None")


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next  # Save next node
            curr.next = prev  # Reverse the pointer
            prev = curr  # Move prev forward
            curr = next_node  # Move curr forward
        return prev


# @leet end

head_values = [1, 2, 4, 5]

head = ListNode(val=head_values[0])
current = head

for i in range(1, len(head_values)):
    current.next = ListNode(val=head_values[i])
    current = current.next

sol = Solution()
print(sol.reverseList(head))

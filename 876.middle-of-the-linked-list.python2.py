# @leet start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # slow = head
        # fast = head
        # while fast and fast.next:
        #     fast = fast.next.next  # Move fast two steps
        #     slow = slow.next  # Move slow one step
        # return slow

        fast = head
        slow = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

        return slow


# @leet end


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head_ = [1, 7, -3, 43]
head = ListNode(head_[0])
current = head

for i in range(1, len(head_)):
    current.next = ListNode(val=head_[i])
    current = current.next

sol = Solution()
print(sol.middleNode(head))

# @leet start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        val = 0
        current = head

        while current:
            val = 2 * val + current.val
            current = current.next

        return val


# @leet end


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head_ = [1, 0, 1, 0]
head = ListNode(head_[0])
current = head

for i in range(1, len(head_)):
    current.next = ListNode(val=head_[i])
    current = head.next

sol = Solution()
print(sol.getDecimalValue(head))

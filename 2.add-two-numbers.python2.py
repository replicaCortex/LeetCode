# @leet start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next


# @leet end

head_ = [9, 9]
head = ListNode(head_[0])
rrent = head

for i in range(1, len(head_)):
    rrent.next = ListNode(val=head_[i])
    rrent = rrent.next

head1 = [9, 9]
head2 = ListNode(head1[0])
current = head2

for i in range(1, len(head1)):
    current.next = ListNode(val=head1[i])
    current = current.next

sol = Solution()
print(sol.addTwoNumbers(head, head2))

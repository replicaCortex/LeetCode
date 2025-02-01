# @leet start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # if head == None:
        #     return head
        #
        # tmp = []
        #
        # current = head
        # new_head = ListNode(val=current.val)
        #
        # tmp.append(current.val)
        # current = current.next
        # new_current = new_head
        #
        # while current:
        #     if current.next != None and current.val not in tmp:
        #         new_current.next = ListNode(val=current.val)
        #         new_current = new_current.next
        #         pass
        #
        #     elif current.next == None and current.val not in tmp:
        #         new_current.next = ListNode(val=current.val)
        #         new_current = new_current.next
        #
        #     tmp.append(current.val)
        #     current = current.next
        #
        # return new_head

        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return res


# @leet end


head_ = [1, 2, 2, 2, 4, 5]
head = ListNode(head_[0])
current = head

for i in range(1, len(head_)):
    current.next = ListNode(val=head_[i])
    current = current.next

sol = Solution()
print(sol.deleteDuplicates(head))

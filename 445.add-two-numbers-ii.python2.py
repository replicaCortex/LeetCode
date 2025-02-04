# @leet start
# Definition for singly-linked list.


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def helper(self, l1, l2):
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = dummyHead.next
        return result

    def addTwoNumbers(self, l1, l2):
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        ans = self.helper(l1, l2)
        return self.reverseList(ans)


# @leet end

# head_ = [1, 2, 4, 5, 1]
head_ = [7, 2, 4, 3]
head__ = [5, 6, 4]
head = ListNode(head_[0])
current = head

for i in range(1, len(head_)):
    current.next = ListNode(val=head_[i])
    current = current.next

# head__ = [2, 3, 5, 6]
head2 = ListNode(head__[0])
current = head2

for i in range(1, len(head__)):
    current.next = ListNode(val=head__[i])
    current = current.next

sol = Solution()

print(sol.addTwoNumbers(head, head2))

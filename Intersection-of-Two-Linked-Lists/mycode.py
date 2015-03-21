# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if (not headA) or (not headB):
            return None
        a = headA
        b = headB
        ans = None
        while a or b:
            if a and b:
                if a.val==b.val:
                    if not ans:
                        ans = a
            if not a:
                a = headB
            if not b:
                b = headA
            a = a.next
            b = b.next
        return ans
    def display(self, root):
        node = root
        while node:
            if not node.next:
                print node.val
            else:
                print node.val, '->',
            node = node.next


headA = ListNode(x = 'a1')
headA.next = ListNode(x = 'a2')
headA.next.next = ListNode(x = 'a3')
headA.next.next.next = ListNode(x = 'c1')
headA.next.next.next.next = ListNode(x = 'c2')

headB = ListNode(x = 'b1')
headB.next = ListNode(x = 'b2')
headB.next.next = ListNode(x = 'c1')
headB.next.next.next = ListNode(x = 'c2')


print '\nFirst ListNode:'
Solution().display(headA)
print '\n'
print 'Second ListNode:'
Solution().display(headB)

print '\n'
print 'The first shared node is:'


print Solution().getIntersectionNode(headA, headB).val

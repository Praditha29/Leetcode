#LEETCODE PROBLEM 876: MIDDLE OF THE LINKED LIST

# Main solution for leetcode
# class Solution(object):
#     def middleNode(self, head):
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow

#---------------------------------------------------------------------------------------------------------------------#
# Detailed solution along with pointer printed
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()

# # Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
# head.next.next.next.next.next.next.next = ListNode(8)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(3)
head = node1

# Connect them normally
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Create the cycle
node5.next = node2

print("Linked list:")
print_list(head)

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            return True
        else:
            print("not cyclic")
        return slow
    
sol = Solution()
middle = sol.middleNode(head)

print("Middle node value:", middle.val)

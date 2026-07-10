class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode(None)
        curr = head
        while list1 or list2:
            if list1 is None:
                curr.next = list2
                return head.next
            if list2 is None:
                curr.next = list1
                return head.next
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else: 
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return head.next

def createLinkedList(arr):
    dummy = ListNode()
    curr = dummy

    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)
printLinkedList(merged)
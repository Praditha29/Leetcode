class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next # curr.next ki value next_node me store hoga (i.e. 2)
            curr.next = prev # curr.next = none
            prev = curr # prev = head mtlb 1
            curr= next_node #curr me next_node ki value mtlb 2
        return prev
    
#during the first iteration:
# next_node = curr.next
# prev curr curr.next
#   ↓   ↓    ↓
#       1 -> 2 -> 3 -> 4 -> 5 ->


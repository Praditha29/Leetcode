def hasCycle(head):
        # Initializing both pointers to head
        slow = head
        fast = head
        # Till there are elements next to fast and after fast (That would mean that the pointer did not reach the end)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # If cycle
                return True
        return False
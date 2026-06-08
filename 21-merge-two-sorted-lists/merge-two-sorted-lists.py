# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1   # append list1 node
                list1 = list1.next
            else:
                current.next = list2   # append list2 node
                list2 = list2.next

            current = current.next    # move pointer

        # append remaining part (like extend)
        current.next = list1 if list1 else list2

        return dummy.next
        
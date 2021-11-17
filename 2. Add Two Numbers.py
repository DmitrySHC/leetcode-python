'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_reverse_str(arg):
    if arg.next == None:
        return str(arg.val)
    else:
        return list_to_reverse_str(arg.next) + str(arg.val)


class Solution:
    def add_two_numbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        res = str(int(list_to_reverse_str(l1)) + int(list_to_reverse_str(l2)))
        res_list = tmp = ListNode()
        for i in range(len(res) - 1, -1, -1):
            tmp.next = ListNode(int(res[i]))
            tmp = tmp.next
        return res_list.next

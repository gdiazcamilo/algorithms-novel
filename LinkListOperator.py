from .common import ListNode

class LinkListOperator:
    """
        This class solves the problem: https://leetcode.com/problems/add-two-numbers/
        
        Assumptions:
            Numbers are non negative.
            Only one digit per node.


        The problem is solved using an O(n) memory and O(n) runtime approach.

        The approach is iterate while we have a node to process to some remaining carry value from the last sum of digits.
        In any of this case we are going to create a new node and append the node to the list we are going to return.

        To build the new list we use keep a reference to the head and use another variable to keep a reference to the 
        last inserted node in the list so we can continue append new elements.

    """

    def add_lists(self, head1: ListNode, head2: ListNode):

        result_head = ListNode()
        result_node = result_head

        node1 = head1
        node2 = head2
        carry = 0
        while node1 or node2 or carry > 0:
            value = node1.val if node1 else 0
            value += node2.val if node2 else 0
            value += carry

            # In case of double digit number, this will be one; else zero.
            carry = value // 10
            
            # In case of double digit number, this will be the first digit.
            new_digit = value % 10
            
            new_digit_node = ListNode(new_digit)
            result_node.next = new_digit_node
            result_node = result_node.next

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        
        return result_head.next

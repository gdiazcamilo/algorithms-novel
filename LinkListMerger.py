from common import ListNode

class LinkListMerger:
    """
        This class solves the problem: https://leetcode.com/problems/merge-two-sorted-lists/
        The only exposed the method is `merge` that should be called with the test cases.
    """

    def merge(self, first_list_node: ListNode, second_list_node: ListNode):
        """
        Merges two linked list starting at the given nodes (usually the head).

        Returns the head of the merged link list.
        
        The merge is done by splicing together the nodes from the two lists. 
        This means that the two list passed by parameters are modified.
        """


        # Starting with a node before the head (pre head) allow us to avoid a
        # condition inside the loop that would only be useful the first 
        # iteration to set the head or repeating the condition outside the loop. 
        merged_list_pre_head = ListNode()

        # Keep track of the last merged node. This is the pointer that links
        # the next smaller node from the two merging lists.
        last_merged_node = merged_list_pre_head
        
        while self.__comparison_is_possible(first_list_node, second_list_node):
            if first_list_node.val < second_list_node.val:
                last_merged_node.next = first_list_node
                first_list_node = first_list_node.next
            else:
                last_merged_node.next = second_list_node
                second_list_node = second_list_node.next
        
            last_merged_node = last_merged_node.next

        # Take the remaining node (and all subsequent nodes) from the list 
        # that wasn't exhausted and merged it.
        next_node_to_merge = first_list_node or second_list_node
        last_merged_node.next = next_node_to_merge

        return merged_list_pre_head.next
    
    def __comparison_is_possible(self, first_list_node: ListNode, second_list_node: ListNode) -> bool:
        return first_list_node and second_list_node


list1 = ListNode(1, next=ListNode(2, next=ListNode(4)))
list2 = ListNode(1, next=ListNode(3, next=ListNode(4)))
assert list2.next.val == 3

merger = LinkListMerger()
merged_list = merger.merge(list1, list2)
print(merged_list)

assert list2.next.val == 1
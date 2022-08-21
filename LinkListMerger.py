from common import ListNode

class LinkListMerger:

    def merge(self, node1, node2):
        """
        Merges two linked list starting at the given nodes (usually the head)
        """


        # Starting with a node before the head (pre head) allow us to avoid a
        # condition inside the loop that would only be useful the first 
        # iteration to set the head or repeating the condition outside the loop. 
        merge_list_pre_head = ListNode()

        # Keep track of the last merged node. This is the pointer that links
        # the next smaller node from the two merging lists.
        last_merged_node = merge_list_pre_head

        while node1 and node2:
            if not node1 or (node2 and node2.val < node1.val):
                last_merged_node.next = node2
                last_merged_node = last_merged_node.next
                node2 = node2.next
            else:
                last_merged_node.next = node1
                last_merged_node = last_merged_node.next
                node1 = node1.next
            
        return merge_list_pre_head.next

list1 = ListNode(1, next=ListNode(2, next=ListNode(4)))
list2 = ListNode(1, next=ListNode(3, next=ListNode(4)))

l1_pointer = list1
l2_pointer = list2

merger = LinkListMerger()
merged_list = merger.merge(list1, list2)
print(merged_list)

assert list1 == l1_pointer
assert list2 == l2_pointer
from collections import Counter
from typing import List


class KthLargestFinder:
    """
        This class solves the problem: https://leetcode.com/problems/kth-largest-element-in-an-array/
        
        Assumptions:
            The integers in the array are not sorted, could include repeated and negative numbers.
        
        Limitations:
            Can't use the sort built-in method.

        The problem is solved using an O(n) memory and O(m) runtime approach. Where m is the max number in the input array.
        The idea is to identify the max number and then count backwards to see if lower numbers are in the array, 
        repeat that K times (the times that a number is found). Using a dictionary instead of a set to account for the duplicated numbers.
    """

    def findKthLargest(self, numbers: List[int], kth_largest: int) -> int:
        """
            Args:
                numbers: Array of integers where would be loop up the kth largest
                kth_largest: Integer indicating the largest Kth element. 1 is the largest of all.
            Returns
                The largest Kth integer in `numbers` 
        """

        numbers_count = Counter(numbers)
        max_number = max(numbers)
        largest_kth_so_far = 1

        while largest_kth_so_far < kth_largest:
            max_number_is_present = max_number in numbers_count and numbers_count[max_number] > 0
            if max_number_is_present:
                numbers_count[max_number] -= 1
                largest_kth_so_far += 1
            else:
                max_number -= 1
        
        return max_number
        
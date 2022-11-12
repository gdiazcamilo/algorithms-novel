from typing import List


class SequenceFinder:
    """
        This class solves the problem: https://leetcode.com/problems/longest-consecutive-sequence/
        
        Limitations:
            Can't use sort built-in method

        The problem is solved using O(n) memory and O(n) runtime.

        Built a set from the original numbers list. 
        Iterate the numbers looking for the end of the sequence. Using a set,
        makes this efficient because we can check in O(1) if the number doesn't 
        have a continuation. If so, we start counting backwards until the first 
        number of the sequence, meaning when the element we're decreasing by 1 
        is no longer in the set.
    """


    def find_longest_consecutive_sequence(self, numbers: List[int]) -> int:
        numbers_set = set(numbers)
        longest_sequence_size = 0

        for curr_number in numbers_set:
            curr_number_is_last_sequence_number = (curr_number + 1) not in numbers_set
            
            if curr_number_is_last_sequence_number:
                previous_number = n - 1
                sequence_size = 1

                while previous_number in numbers_set:
                    sequence_size += 1
                    previous_number -= 1
                
                longest_sequence_size = max(longest_sequence_size, sequence_size)

        return longest_sequence_size
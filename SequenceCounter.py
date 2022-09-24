from enum import unique
from typing import List


class SequenceCounter:
    """
        This class solves the problem: https://leetcode.com/problems/longest-consecutive-sequence/
        
        The problem is solved using an O(n) memory approach and O(n) runtime.

        The idea is to find the last number of a sequence and then count backwards to the first number of the sequence
        using a set to check if the consecutive number is present and save lots of time.
    """


    def __init__(self, numbers: List[int]) -> None:
        self.sequence_numbers = set(numbers)
    

    def set_sequence_numbers(self, numbers: List[int]) -> None:
        self.sequence_numbers = set(numbers)


    def count_longest_consecutive_sequence(self) -> int:
        """
            Returns the number of elements in the longest consecutive sequence 
            present in the `numbers` array.
        """

        longest_sequence = 0

        for number in self.sequence_numbers:
            if self.__is_end_of_sequence(number):
                sequence_count = self.__count_numbers_in_sequence(number)

                if sequence_count > longest_sequence:
                    longest_sequence = sequence_count
        
        return longest_sequence


    def __count_numbers_in_sequence(self, final_number):
        """
            Returns the number of consecutive elements present in the
            `sequence_numbers`, starting at `final_number` and counting backwards
        """

        sequence = 1
        previous_number = final_number - 1
        while previous_number in self.sequence_numbers:
            sequence += 1
            previous_number -= 1
        
        return sequence

    def __is_end_of_sequence(self, number):
        next_number = number + 1
        return next_number not in self.sequence_numbers
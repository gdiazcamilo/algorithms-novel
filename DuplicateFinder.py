from abc import ABC, abstractmethod
from socket import J1939_EE_INFO_NONE

from typing import List


class DuplicateFinder(ABC):
    """
        This class define the interface for solving the problem: https://leetcode.com/problems/find-the-duplicate-number/
        
        That problem has many solutions. Subclasses implement different solutions for the problem. 
        Assumptions:
            The numbers contained in the array will be in the range 1 to n and the length of the array will be n + 1
            The given array will always have one number that repeats itself at least one time.

    """

    @abstractmethod
    def find_duplicate(self, numbers: List[int]) -> int:
        pass
        

class NegativeMarkerDuplicateFinder(DuplicateFinder):
    """
        This class use the negative marker approach for solving the problem: https://leetcode.com/problems/find-the-duplicate-number/

        Given the assumptions stated in the parent class we can use the negative marker approach.
        In this approach we use the numbers in the array as indexes to visit other positions in the array,
        mark the visited positions by making the number negative and when we find a duplicated number we'll end up
        visiting a repeated position, so we know that index is the duplicate number.
    """

    def find_duplicate(self, numbers: List[int]) -> int:
        current_position = 0
        duplicate_number = None
        while duplicate_number is None:
            if self.__position_was_visited(numbers, current_position):
                duplicate_number = current_position
            else:
                # The use of two variables here is for clarity. It represents 
                # better the intention: the visited number at the current_position 
                # is going to be the next position we are going to check in the next iteration.
                visited_number = self.__mark_visited_position(numbers, current_position)
                current_position = visited_number
        
        # Make the array as it was originally.
        self.__remove_visited_markers(numbers)
        
        return duplicate_number
    
    
    def __position_was_visited(self, numbers: List[int], idx) -> bool:
        """
            Returns True if the `idx` has been visited. 
        """

        # When a number is visited is marked as negative.
        return numbers[idx] <= 0
    

    def __mark_visited_position(self, numbers: List[int], visited_idx) -> None:
        """
            Changes the number at `visited_idx` to negative.
            
            Returns the number at `visited_idx` (aka. the visited number).
        """

        visited_number = numbers[visited_idx]
        numbers[visited_idx] = -numbers[visited_idx]
        return visited_number 

    
    def __remove_visited_markers(self, numbers: List[int]) -> None:
        """
            Revert back the negative numbers to positives.
        """

        for idx in range(len(numbers)):
            if numbers[idx] < 0:
                numbers[idx] = -numbers[idx]
    


class BinarySearchDuplicateFinder(DuplicateFinder):
    """
        This class use the binary search approach for solving the problem: https://leetcode.com/problems/find-the-duplicate-number/

        If we have an array with numbers from 1 to n and one duplicate, we can split the range into two halves and say that from 1 to n/2 
        there should be n/2 elements in the array. So, we count the number of elements in the array and if the count is bigger then we know 
        that duplicated number is in the first half, otherwise is on the second half.
        We repeat this process until the range only contains one number which will be the duplicate number.
    """

    START = 0
    END = 1

    def find_duplicate(self, numbers: List[int]) -> int:
        element_count = len(numbers)
        first_possible_duplicate = 1
        last_possible_duplicate = element_count - 1
        
        while self.__number_of_elements_in_range(first_possible_duplicate, last_possible_duplicate) > 1:
            first_half_start = first_possible_duplicate
            first_half_end = self.__range_middle_number(first_possible_duplicate, last_possible_duplicate)
            
            first_half_contains_duplicate = self.__range_contains_duplicate(first_half_start, first_half_end, numbers)
            if first_half_contains_duplicate:
                last_possible_duplicate = first_half_end
            else:
                first_possible_duplicate = first_half_end + 1
        
        assert first_possible_duplicate == last_possible_duplicate
        return first_possible_duplicate


    def __range_middle_number(self, range_start, range_end):
        """
        Returns the middle number of a range.
        """
        return (range_start + range_end) // 2


    def __range_contains_duplicate(self, first_half_start, first_half_end, numbers):
        """
        Returns True if the a duplicate number in `number` is within the start and end of the range.

        The check is done by comparing the count of the elements in the range 
        with the count of how many of those elements are actually in the array `numbers`.
        """

        first_half_expected_count = self.__number_of_elements_in_range(first_half_start, first_half_end)
        first_half_actual_count = self.__count_elements_in_range(numbers, first_half_start, first_half_end)

        return first_half_actual_count > first_half_expected_count


    def __number_of_elements_in_range(self, range_start, range_end):
        """
        Returns the number of sequential elements in the range including start and end.
        """
        return range_end - range_start + 1
    

    def __count_elements_in_range(self, numbers, range_start, range_end):
        """
        Returns the number of elements in the array `numbers` that are 
        between the start and end of the range (inclusive).
        """

        return sum([1 for n in numbers if range_start <= n <= range_end])
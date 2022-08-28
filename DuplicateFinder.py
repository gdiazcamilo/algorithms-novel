from abc import ABC, abstractmethod
from typing import List


class DuplicateFinder(ABC):
    """
        This class define the interface for solving the problem: https://leetcode.com/problems/find-the-duplicate-number/
        
        That problem has many solutions. Subclasses implement different solution approaches for the problem. 
        Assumptions:
            The numbers contained in the array will be in the range 1 to n and the length of the array will be n + 1
            The given array will always have one duplicate.

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

    def find_duplicate(self, numbers: List[int]) -> int:
        return super().find_duplicate(numbers)



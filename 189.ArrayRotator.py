from collections import deque
from typing import List
from abc import abstractmethod, ABC


class ArrayRotator(ABC):

    """
        This class provides the definition method for solving the problem: https://leetcode.com/problems/rotate-array/
        
        Subclasses inherit from this ABC to override the `make_rotate` method with different approaches varying per class.

        Limitations:
            The list received by parameters should be modified in-place. Don't return a new list.
    """

    
    def rotate(self, nums: List[int], rotations: int) -> None:
        actual_rotations = self.simplify_rotations(nums, rotations)
        self.make_rotation(nums, actual_rotations)


    def simplify_rotations(self, nums: List[int], rotations: int):
        return rotations % len(nums)

    
    @abstractmethod
    def make_rotation(self, nums: List[int], rotations: int) -> None:
        pass


class SimpleArrayRotator(ArrayRotator):

    """
    The approach here is O(N x M). Where N is the number of elements in the list and M the number of rotations.
    For every rotation (iteration), all the elements in the array are going to shift position by one as a 
    consequence of inserting at the first index.
    """

    def make_rotation(self, nums: List[int], rotations: int) -> None:
        for _ in range(rotations):
            self._insert_at_beginning(nums, self._pop_from_end(nums))


    def _insert_at_beginning(self, nums: List[int], element: int):
        nums.insert(0, element)
    
    
    def _pop_from_end(self, nums: List[int]) -> int:
        return nums.pop()


class QueueArrayRotator(SimpleArrayRotator):

    """
    This approach is an optimization of the SimpleArrayRotator using a deque which are faster for 
    appending/removing elements at both start/end.
    
    This solution is O(n) runtime and memory. Where N is the number of elements.
    """

    def make_rotation(self, nums: List[int], rotations: int) -> None:
        queue = deque(nums)

        for _ in range(rotations):
            self._insert_at_beginning(nums, self._pop_from_end(nums))
        
        for idx, n in enumerate(queue):
            nums[idx] = n
    

    def _insert_at_beginning(self, nums: deque, element: int):
        nums.appendleft(element)


class ExtraArrayRotator(ArrayRotator):

    """
    This approach uses an extra array and insert the rotated elements backwards. 
    Then merge rotated elements with the non-rotated and updates the original array.

    This is O(n) run time and memory. Where N is the number of elements.
    """

    def make_rotation(self, nums: List[int], rotations: int) -> None:            
        rotated_elements = [None] * rotations
        rotated_element_idx = rotations - 1
        element_to_rotate_idx = len(nums) - 1

        for _ in range(rotations):
            rotated_elements[rotated_element_idx] = nums[element_to_rotate_idx]
            rotated_element_idx -= 1
            element_to_rotate_idx -= 1
        
        rotated_elements.extend(nums[:element_to_rotate_idx + 1])
        
        for idx, e in enumerate(rotated_elements):
            nums[idx] = e


class SplitArrayRotator(ArrayRotator):

    """
    The approach here is to calculate the index of the rotation point. 
    The elements from that point to the end of the array will be the first elements.

    This is O(n) run time and memory. Where N is the number of elements.
    """

    def make_rotation(self, nums: List[int], rotations: int) -> None:
        rotation_point = len(nums) - rotations
        first_elements = nums[rotation_point:]
        second_elements = nums[:rotation_point]
        
        idx = 0
        for e in first_elements:
            nums[idx] = e
            idx += 1
        
        for e in second_elements:
            nums[idx] = e
            idx += 1
    

class ReverseArrayRotator(ArrayRotator):

    """
    This is the less intuitive, but most memory efficient approach. The runtime is O(n) and memory is constant.

    We find a rotation point where elements from that point to the end are going to be shifted to the beginning of the array.
    Rotate the entire array, and then rotate part before and after the rotation point independently.

    [1,2,3,4,5,6] ; rotations = 3
    [6,5,4,3,2,1] # step 1: rotate entire array
    [4,5,6, 3,2,1] # step 2: rotate the number of elements specified
    [4,5,6, 1,2,3] # step 3: rotate back the other part of the array.
    """

    def reverse(nums: List[int], start_idx, end_idx) -> None:
        while start_idx < end_idx:
            nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
            start_idx += 1
            end_idx -= 1
    
    def make_rotation(self, nums: List[int], rotations: int) -> None:
        self.reverse(0, len(nums) - 1)
        self.reverse(0, rotations - 1)
        self.reverse(rotations, len(nums) - 1)
    
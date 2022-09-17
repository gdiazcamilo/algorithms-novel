from typing import List


class ColorsSorter:
    """
        This class solves the problem: https://leetcode.com/problems/sort-colors/
        
        Assumptions:
            The numbers in the array will be 0, 1 or 2. Each number represent red, white and blue respectively.
        
        Limitations:
            Can't use the sort built-in method. Anyway the best we can do is O(n log n) using built-in sort.

        The problem is solved using an in-place and constant memory approach and O(n) runtime.
        The idea is to put the red (0) at the start, the blues (2) at the end and with that the whites (1) should 
        be in the middle and the array sorted.
    """



    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED = 0
        WHITE = 1
        BLUE = 2
        
        current_idx = 0
        next_red_idx = 0
        next_blue_idx = len(nums) - 1
        
        while self.__pending_elements_to_sort(current_idx, next_blue_idx):
            current_color = nums[current_idx]
            
            if current_color == RED:
                # Always next_red_idx will be equal or less than current_idx.
                # The color at next_red_idx is going to be white or red.
                nums[current_idx] = nums[next_red_idx]
                nums[next_red_idx] = RED
                next_red += 1
                current_idx += 1
            
            elif current_color == WHITE:
                # By putting reds at the beginning and blues at the end, 
                # the whites will be in the middle. No need to do anything.
                current_idx += 1
            
            else:
                # We don't know the color at next_blue_idx, so we put it at current_idx
                # but don't increase current_idx. It will be handle in the next iteration.
                nums[current_idx] = nums[next_blue_idx]
                nums[next_blue_idx] = BLUE
                next_blue_idx -= 1
    
    
    def __pending_elements_to_sort(current_idx, next_blue_idx):
        return current_idx <= next_blue_idx
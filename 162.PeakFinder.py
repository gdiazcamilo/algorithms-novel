from typing import List


class PeakFinder:
    """
        This class solves the problem: https://leetcode.com/problems/find-peak-element/
        
        Assumptions:
            - Numbers outside the array are considered always lower (-infinity).
            - Contiguous elements are never the equal

        The problem is solved using a constant memory approach and O(log n) runtime.

        We do binary search and always check if we are in a peak. 
        If not, move the pointers to any side that is higher than current.
    """

    def find_peak(self, numbers: List[int]) -> int:
        from_idx = 0
        to_idx = len(numbers) - 1

        while from_idx <= to_idx:
            middle_idx = (from_idx + to_idx) // 2
            middle_num = numbers[middle_idx]

            left_number = numbers[middle_idx - 1] if middle_idx > 0 else float('-inf')
            right_number = numbers[middle_idx + 1] if middle_idx < len(numbers) - 1 else float('-inf')

            if left_number < middle_num > right_number:
                return middle_idx
            elif left_number > middle_num:
                to_idx = middle_idx - 1
            else:
                from_idx = middle_idx + 1
        
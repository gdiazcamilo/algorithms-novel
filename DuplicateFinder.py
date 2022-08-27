from abc import ABC, abstractmethod
from typing import List


class DuplicateFinder(ABC):

    @abstractmethod
    def find_duplicate(self, numbers: List[int]) -> int:
        pass

class NegativeMarkerDuplicateFinder(DuplicateFinder):

    def find_duplicate(self, numbers: List[int]) -> int:
        
        next_idx = 0
        duplicate_number = None
        while next_idx < len(numbers):
            if numbers[next_idx] <= 0:
                duplicate_number = abs(numbers[next_idx])
                break

            numbers[next_idx] = -numbers[next_idx]
            next_idx = abs(numbers[next_idx])
        
        for idx in range(len(numbers)):
            if numbers[idx] < 0:
                numbers[idx] = -numbers[idx]
        
        return duplicate_number


class BinarySearchDuplicateFinder(DuplicateFinder):

    def find_duplicate(self, numbers: List[int]) -> int:
        return super().find_duplicate(numbers)



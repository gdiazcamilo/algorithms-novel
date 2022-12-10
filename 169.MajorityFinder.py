

from abc import abstractmethod, ABC
from collections import Counter, defaultdict
from typing import List


class MajorityFinder(ABC):
    """
    Abstract Base Class to solve: https://leetcode.com/problems/majority-element/description/
    """

    @abstractmethod
    def find_majority(self, elements: List[int]):
        pass


class MajoritySortingFinder(MajorityFinder):
    """
    Time: O(N log N)
    Space: O(N)

    Since the majority element will be repeating at least more time than the half of the list
    we can sort the list and the middle element will always be the majority.
    """

    def find_majority(self, elements: List[int]):
        sorted_elements = sorted(elements)
        half_idx = len(sorted_elements) // 2
        return sorted_elements[half_idx]
    

class MajorityDictFinder(MajorityFinder):
    """
    Time: O(N)
    Space: O(N)

    Count how many times appear an element, when found a element that appears more than
    half of the times, that's the majority.
    """

    def find_majority(self, elements: List[int]):
        elements_count = defaultdict(int)
        half = len(elements) // 2

        for element in elements:
            elements_count[element] += 1

            if elements_count[element] > half:
                return element


class MajorityVotingFinder(MajorityFinder):
    """
        Time: O(N)
        Space: O(1)

        This is the Boyer-Moore Voting Algorithm.
        Keep track of the majority element so far, when the element appear again add 1 
        to the occurrences, if found a different element subtract 1 to the occurrences.
        This way the elements will cancel each other and we'll end up with the majority 
        since appear more than all the other elements.
    """
    def find_majority(self, elements: List[int]):
        majority_element = None
        occurrences = 0

        for element in elements:
            if occurrences <= 0:
                majority_element = element

            occurrences += 1 if element == majority_element else - 1
        
        return majority_element
            
from collections import Counter


class CustomStringSorter:
    """
    This class solves the problem: https://leetcode.com/problems/custom-sort-string/

    The approach is O(n) memory and runtime. 
    We count how many of each letter is present in the string. 
    Then iterate the order string and find the number of times each letter in order
    appears in the dict of the letter_count, create a new string and append it to the list
    that is holding the end result custom sorted string.

    """

    def customSortString(self, order: str, s: str) -> str:
        letter_count = Counter(s)
        
        sorted_letters = []
        for order_letter in order:
            if order_letter in letter_count:
                occurrences = letter_count.pop(order_letter)
                sorted_letters.append(order_letter * occurrences)
        
        for letter, occurrences in letter_count.items():
            sorted_letters.append(letter * occurrences)
        
        return ''.join(sorted_letters)
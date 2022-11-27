from collections import Counter


class CustomStringSorter:

    def customSortString(self, order: str, s: str) -> str:
        letter_count = Counter(s)
        
        sorted_letters = []
        for order_letter in order:
            if order_letter in letter_count:
                sorted_letters.append(order_letter * letter_count.pop(order_letter))
        
        for letter, occurrences in letter_count.items():
            sorted_letters.append(letter * occurrences)
        
        return ''.join(sorted_letters)
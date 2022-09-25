from unicodedata import digit


class DigitsRemover:
    """
        This class solves the problem: https://leetcode.com/problems/remove-k-digits/
        
        The problem is solved using an O(n) memory approach and O(n) runtime.

        The approach is to remove the most significant digits from the left and then from the right.
        When the previous digit (from left to right) is greater than the current one, then we say
        the previous digit is more significant. 
        So, in the sequence: 12345, 5 (at the rightmost) is the most significant; 
        in the sequence: 54321, it's 5 (at the leftmost)
    """

    def __init__(self, digits_to_remove: int) -> None:
        self.remaining_digits = []
        self.digits_to_remove = digits_to_remove
    

    def set_digits_to_remove(self, digits_to_remove: int):
        self.digits_to_remove = digits_to_remove


    def remove_digits(self, number: str) -> str:
        """
            Removes the most significant digits from the `number` argument.
            The number of significant digits to remove is given by `digits_to_remove` property.
        """

        assert (len(number) >= self.digits_to_remove, 
            "The number of digits to remove can't be greater than the length of"
            " the number")
        
        self.remove_most_significant_digits(number)
        
        # After removing the most significant digits from the left, if there are
        # pending removals, these must be necessarily on the right (last digits)
        while self.pending_removals():
            self.remove_last_digit()
        
        return self.remaining_digits_as_string()
    

    def remaining_digits_as_string(self) -> str:
        """
            Returns the remaining digits as a single sanitized number string 
            or '0' if all digits were removed.
        """

        number = ''.join(self.remaining_digits)
        
        # remove leading zeros
        number = int(number or '0')

        return str(number)


    def remove_most_significant_digits(self, number: str) -> None:
        """
            Remove the most significant digits from left to right. 
            The maximum number of removals is given by `digits_to_remove` property.
        """

        # Always we remove a digit which is greater than the previous one, we'll
        # get a smaller number.
        for current_digit in number:
            while (self.pending_removals() and
                self.last_digit_is_more_significant_than(current_digit)):
                self.remove_last_digit()
            
            self.add_current_digit(current_digit)
            
    
    def pending_removals(self) -> bool:
        return self.digits_to_remove > 0


    def last_digit_is_more_significant_than(self, current_digit: int) -> bool:
        """
            Returns True if the last digit in `remaining_digits` prop is 
            greater than the `current_digit` arg. False otherwise or when there
            are no digits in `remaining_digits`.
        """

        return self.remaining_digits and self.remaining_digits[-1] > current_digit


    def remove_last_digit(self):
        self.remaining_digits.pop()
        self.digits_to_remove -= 1


    def add_current_digit(self, current_digit: int):
        self.remaining_digits.append(current_digit)

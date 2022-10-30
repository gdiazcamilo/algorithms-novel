class SmallestDigitConverter:
    """
        This class solves the problem: https://leetcode.com/problems/remove-k-digits/
        
        Assumptions:
            Number is positive.
            Number of removals is less or equal than the number's length.


        The problem is solved using an O(n) memory and O(n) runtime approach.

        The approach is to remove the most significant digits from left to right. In a way that the current digit
        is always is largest digit. So we end up with a sequence of digits in ascending order like '2456789'. 
        After that, the if there are still remaining digits, necessarily are in the right end, so we remove the 
        pending removals from the right- end

    """

    def remove_k_digits(self, number: str, k: int) -> str:
        remaining_digits = []
        removals_count = 0

        # Remove the most significant digits from left to right.
        # It's important to start with the left, for cases like '20050'
        for digit in number:
            while self.can_remove_digit() and self.remains_larger_digits(remaining_digits, digit):
                remaining_digits.pop()
                removals_count += 1
            
            remaining_digits.append(digit)

        # Remove the remaining most significant digits from right to left.
        # After removing the digits from left-to-right we end up with a sequence of 
        # digits in increasing order. So the largest digits are at the right end.
        remaining_removals = k - removals_count
        if remaining_removals:
            remaining_digits = remaining_digits[:-remaining_removals]
        
        result = ''.join(remaining_digits) or '0'
        return str(int(result))


    def can_remove_digit(self, remaining_digits, removals_count, max_removals):
        return remaining_digits and removals_count < max_removals


    def remains_larger_digits(self, remaining_digits, current_digit):
        return remaining_digits[-1] > current_digit 
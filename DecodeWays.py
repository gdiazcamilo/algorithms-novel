class Decoder:

    def get_decoding_ways(self, encoded_digits: str) -> int:
        """
            Returns an integer indicating how many possible ways the encoded
            string can be decoded.

            It assumes the encoded_digits params contains only digits. 
            
            The decoding way up to a position in the string depends on the current and previous digit.
            We have 4 cases:
                1. The digits can't be decoded. It happens when it's not possible to form a number between 1 and 26. In this case we abort and return 0.
                2. The digits can only be used combined. Basically 10 or 20. The decoding ways up to those digits is the decoding ways of two digits before (skip the ways of the digit before because the digits must be combined and treated as a single digit.)
                3. The digits can be combined or single. This is any number between 11 and 19 and 21 and 26. The decoding ways up to those digits is the sum of the previous ways of the two digits before.
                4. The digits can only be single. This happens for numbers greater than 26 (excluding the ones that ends with 0) or less than 10. The decoding way will be the same as the previous one.
            
            Example:
                Digits      |   1   |   2   |   1   |   0   |   9   |   0
                Ways    1*  |   1   |   2   |   3   |   2   |   2   |   0
                Case        |   4   |   3   |   3   |   2   |   4   |   1

                * Start with one. This is the base case for convenience.
        """

        # Check the first digit outside the loop allow us to 
        # avoid checks for out of bound indexes  or conditions that 
        # will only apply to the first iteration.
        if not self.__first_digit_can_be_decoded(encoded_digits):
            return 0

        penultimate_decoding_ways = 1
        last_decoding_ways = 1

        for previous_digit, current_digit in self.__encoded_digits(encoded_digits):
            previous_decoding_ways = last_decoding_ways

            if self.__can_not_be_decoded(previous_digit, current_digit):
                return 0

            if self.__digits_must_be_combined(previous_digit, current_digit):
                last_decoding_ways = penultimate_decoding_ways
            elif self.__digits_can_be_combined_or_single(previous_digit, current_digit):
                last_decoding_ways += penultimate_decoding_ways
            
            penultimate_decoding_ways = previous_decoding_ways
        
        return last_decoding_ways


    def __first_digit_can_be_decoded(self, encoded_digits: str):
        """
        Check if the first digit is not zero ('0').

        Zero doesn't map to any letter in the alphabet, being A=1, B=2... Z=26.
        Zero is only valid if it's preceded by an 1 or 2 to form a 10 or 20.
        """

        first_digit = encoded_digits[0]
        return first_digit != '0'

        
    def __encoded_digits(self, encoded_digits):
        for digit_idx in range(1, len(encoded_digits)):
            previous_digit = encoded_digits[digit_idx - 1]
            current_digit = encoded_digits[digit_idx]
            yield previous_digit, current_digit


    def __can_not_be_decoded(self, previous_digit, current_digit):
        return current_digit == '0' and previous_digit not in '12'


    def __digits_must_be_combined(self, previous_digit, current_digit):
        return previous_digit in '12' and current_digit == '0' 


    def __digits_can_be_combined_or_single(self, previous_digit, current_digit):
        """
        Returns true if the digits can form a number between 11 and 26 excluding 20.
        10 and 20 are special cases handled in other method.
        """
    
        return (previous_digit == '1' or 
            (previous_digit == '2' and current_digit in '123456'))


decoder = Decoder('121')
print(decoder.get_decoding_ways())
assert  decoder.get_decoding_ways() == 3
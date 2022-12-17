from typing import List


class WordBreaker:
    """
    This class solves: https://leetcode.com/problems/word-break/

    Time complexity: O(n^3)
    Space complexity: O(n)

    Evaluate if incremental partitions of the string are in wordDict.
    When one partition is in the dict, repeat the process with the remaining portion of the string; if 
    it's not in the dict keep increasing the partition. The `memo` is for optimization purposes.
    """

    def can_break_word(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def can_break(start_idx):
            if start_idx >= len(s):
                return True
            
            if start_idx in memo:
                return memo[start_idx]

            for end_idx in range(start_idx + 1, len(s) + 1):
                partition = s[start_idx : end_idx]
                if partition in wordDict:
                    # only return when can_break is true because we 
                    # want to try to others partitions
                    if can_break(end_idx):
                        return True
            
            # only need to remember the False cases because the function we 
            # need to reach the end of the string to know if the string can be break.
            # Only one time is going to be True.
            memo[start_idx] = False
            return False
        
        return can_break(0)
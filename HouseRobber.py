class HouseRobber:
    """
        This class solves the problem: https://leetcode.com/problems/house-robber/
        
        Assumptions:
            The money in the house is always >= 0

        The problem is solved using a constant memory approach and O(n) runtime.

        While iterating the houses we are going to hold the maximum we can 
        rob so far considering the case when robbing the current house in the 
        iteration and excluding it.

        The max including the current house is going to be the money in the 
        current house plus the accumulated so far by excluding the current.

        The max excluding the current house is going to be the maximum between
        the actual value itself so far and the previous max (before updating it)
        that include the current house, meaning when we move to the next iteration
        the previous value of the variable the holds the max including current
        house can potentially become the value of the max excluding the current 
        house.
    """

    def rob(self, houses):
        max_robbing_current = 0
        max_excluding_current = 0

        for money in houses:
            temp = max_robbing_current

            max_robbing_current = money + max_excluding_current

            max_excluding_current = max(temp, max_excluding_current)

        return max(max_excluding_current, max_robbing_current)
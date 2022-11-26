from typing import List


class GasStation:

    """
    This class solves the problem: https://leetcode.com/problems/gas-station/

    Assumptions:
        Gas and Cost arrays have the same size.

    If the total gas is equal or greater than the total cost then for sure we can travel the entire circuit,
    we just need to find where to start. If we start at a station and from there we can go to the end 
    of the circuit without running out of gas, then that must be the station where we must begin.
    It doesn't matter if that station is the first or the last or one in between, because
    the total gas is greater or equal than the total cost.
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        balance = 0
        gas_in_tank = 0
        starting_station = 0
        for station, (gas_at_station, travel_cost) in enumerate(zip(gas, cost)):
            balance += gas_at_station - travel_cost
            gas_in_tank += gas_at_station - travel_cost
            if gas_in_tank < 0:
                gas_in_tank = 0
                starting_station = station + 1
        
        is_possible_to_complete_circuit = balance >= 0
        return starting_station if is_possible_to_complete_circuit else -1
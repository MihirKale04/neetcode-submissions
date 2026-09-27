class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #we need some way to store if a gas station has been visited or not
            #we move left to right/ if at end jump to begining
                #if we reach a cell that has been visited we have found a cycle
        #the value of each station could potentially be meausured by gas - cost after moving to next
        

        #if the total gas is less than the total cost than it is not possible to complete the circuit
        if sum(gas) < sum(cost):
            return -1
        res = 0
        total = 0
        n = len(gas)
        for i in range(n):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        return res            





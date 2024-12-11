class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start = ind = gas_left = 0
        n = len(gas)

        while start < n : 
            if gas[start] < cost[start]:
                start += 1
                continue
            ind = start

            gas_left = gas[ind] - cost[ind]
            ind = (ind + 1) % n
            
            while gas_left > 0 and ind != start:
                gas_left += (gas[ind] - cost[ind])
                ind = (ind + 1) % n

            if ind == start  and gas_left > -1:
                return start
            elif ind > start :
                start = ind
            else:
                return -1

        return -1

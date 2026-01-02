import heapq

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        surplus = []

        # records the surplus
        for index in range(len(gas)):
            difference = gas[index] - cost[index]
            surplus.append(difference)

        if sum(surplus)<0:
            return -1
        heap = []
        for index, number in enumerate(surplus):
            heapq.heappush(heap,(-number,index))


        while len(heap):
            largest_tuple = heapq.heappop(heap)
            station = largest_tuple[1]
            result = self.canReach(gas,cost,station)
            if result:
                return station
        return -1

    def canReach(self, gas: list[int], cost: list[int], start:int):
        #check if we can travel circularly starting from station
        current_gas = gas[start]
        current_cost = cost[start]
        current_station = start
        while current_gas >= current_cost:
            # go to the next station
            current_station = (current_station +1) %len(gas)
            current_gas -= current_cost
            # if we arrive at our starting point
            if current_station == start:
                return True
            # fill up
            current_gas += gas[current_station]
            current_cost = cost[current_station]

        return False


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:


s = Solution()
# result = s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
# result = s.canCompleteCircuit([2,3,4], [3,4,3])
result = s.canCompleteCircuit([5,8,2,8],[6,5,6,6])


print(result)










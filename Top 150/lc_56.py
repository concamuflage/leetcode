import heapq

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:


        if len(intervals) == 1:
            return intervals

        result = []
        heap=[]
        # sort the intervals using a heap

        for list in intervals:
            heapq.heappush(heap,list)
        prev = heapq.heappop(heap)

        # combine new with prev if they overlap.
        # else, just put the new interval in the result and set it to the new prev.

        while heap:
            new = heapq.heappop(heap)
            if self.overlap(prev,new):
                prev = self.combine(prev,new)
            else:
                result.append(prev)
                prev = new
        result.append(prev)
        return result

    def overlap(self,tuple1,tuple2):
        if tuple1[1] >= tuple2[0]:
            return True
        return False
    def combine(self,tuple1,tuple2):
        return (tuple1[0],max(tuple1[1],tuple2[1]))


s = Solution()
intervals= [[1,2]] # [1,2]
print(s.merge(intervals))
intervals = [[1,2],[3,4]]
print(s.merge(intervals))  #[1,2],[3,4]

intervals = [[1,3],[2,4]]
print(s.merge(intervals))  #[1,4]
intervals = [[1,2],[2,4]]
print(s.merge(intervals))  #[1,4]

intervals = [[1,2],[2,4],[5,7]]
print(s.merge(intervals))  #[1,4],[5,7]
intervals = [[1,2],[2,4],[3,4],[5,7]]
print(s.merge(intervals))  #[1,4],[5,7]
intervals = [[1,2],[2,4],[3,5],[5,7]]
print(s.merge(intervals))  #[1,7]

intervals = [[1,2],[2,4],[3,4],[5,7],[7,8]]
print(s.merge(intervals))  #[1,4],[5,8]

intervals = [[1,2],[2,4],[3,4],[5,7],[8,89]]
print(s.merge(intervals))  #[1,4],[5,7],[8,89]

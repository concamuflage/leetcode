import heapq

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        # sorting is important because now we can imagine these intervals on a real number axis.
        # we keep merging when there is an overlap. When there is no overlap at new interval,
        # we can use this new interval as new base and test if it overlaps the ones following it.
        # the ones following the base cannot have an overlap with intervals before the current base.

        intervals.sort(key = lambda x : x[0])
        merged = [intervals[0]]
        for start,end in intervals[1:]:

            pre_start,prev_end = merged[-1]
            if start <= prev_end:
                # we only need to change the end of the previous interval or the previously merged interval
                # both happen to be the last interval in merged.

                merged[-1][1] = max(end,prev_end)
            else:
                merged.append([start,end])
        return merged

s = Solution()
intervals= [[1,2]] # [1,2]
print(s.merge(intervals))
intervals = [[4,7],[1,4]]
print(s.merge(intervals))  #[1,7]

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
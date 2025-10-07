class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self._next_number(n) 

        while fast != 1 and slow != fast:
            slow = self._next_number(slow)
            fast = self._next_number(self._next_number(fast))
        if fast == 1:
            return True
        if slow == fast:
            return False
        

    def _next_number(self,n:int) -> int:

        total = 0
        while n > 0:

            digit = n % 10
            total += digit ** 2
            if digit == 0:
                n = n // 10 
            else:
                n = n - digit
        return total

        

                
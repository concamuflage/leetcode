class Solution:
    def romanToInt(self, s: str) -> int:
        # parse the string from left to right
            # two letters
        total = 0
        special_strings = ["IV", "IX", "XL", "XC", "CD", "CM"]
        # create a window of 2
        left_pointer = 0
        right_pointer = 1


        while right_pointer <= len(s):
            # get a slice of 2
            slice = s[left_pointer:right_pointer+1]
            # slide the window
            if slice in special_strings:
                total += self.convert(slice)
                left_pointer += 2
                right_pointer += 2
            else:
                total += self.convert(slice[0])
                left_pointer += 1
                right_pointer += 1
        return total

    def convert(self,s:str) ->int :
        if s == "I":
            return 1
        elif s == "V":
            return 5
        elif s == "X":
            return 10
        elif s == "L":
            return 50
        elif s == "C":
            return 100
        elif s == "D":
            return 500
        elif s == "M":
            return 1000
        elif s == "IV":
            return 4
        elif s == "IX":
            return 9
        elif s == "XL":
            return 40
        elif s == "XC":
            return 90
        elif s == "CD":
            return 400
        elif s == "CM":
            return 900

        


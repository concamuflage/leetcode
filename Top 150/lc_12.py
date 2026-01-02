class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = []
        literal = ""
        while num != 0:
            key = self.findMaxiumValue(num,keys)
            new_literal = roman_numerals[key]
            result.append(new_literal)
            num -= key
        return "".join(result)

    # my solution is slow because the following method iterate through the keys many times.

    def findMaxiumValue(self,number,keys):
        for key in keys:
            if key <= number:
                return key

s = Solution()
print(s.intToRoman(3749))



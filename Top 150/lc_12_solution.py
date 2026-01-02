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
        for key in keys:
            if num == 0:
                break
            count = num // key
            if count !=0:
                literal = roman_numerals[key]
                result.append(literal*count)
                num = num % key
        return "".join(result)


s = Solution()
print(s.intToRoman(3749))
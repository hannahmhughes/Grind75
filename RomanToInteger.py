# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        numToVal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        lastStep = 'I'
        value = 0

        for char in s[::-1]:
            if numToVal[char] >= numToVal[lastStep]:
                value += numToVal[char]
                lastStep = char
            else:
                value -= numToVal[char]

        return value
        

"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "MCM": (1000-100+1000) = 1900 = (1000+100+1000) -200
        "IV": 1+5 = 6 = V-I = 5-1
        """
        # step1. define parameters
        dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
        # step2. roman to integer
        # method: add and consider special case ex. IV(small,large)--> -2
        result = 0    # initial value
        for c in s:
            result += dict[c]
        if s.find("IV") != -1:
            result -= 2
        if s.find("IX") != -1:
            result -= 2
        if s.find("XL") != -1:
            result -= 20
        if s.find("XC") != -1:
            result -= 20
        if s.find("CD") != -1:
            result -= 200
        if s.find("CM") != -1:
            result -= 200
        return result

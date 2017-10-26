"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""
"""
[Hint]
get the length of string and walk from last index; once meet the blank space, it is a word
and append it as the first word into the new blank string
"""
#### Method 1 ####
class Solution(object):
    def reverseWords(self, s):
        # step1. calculate the string length and define if no words then return blank string
        length = len(s)
        if length < 1:
            return s
        # step2. define parameters
        right_index = length -1
        new_string = ""
        # step3. reverse words; if there is word
        while right_index >= 0:
            ## layer1: trailing blank space in last position
            while right_index >= 0 and ' ' == s[right_index]:
                right_index -= 1
            end_index = right_index
            ## layer2: no trailing blank space in the last word
            while right_index >= 0 and ' ' != s[right_index]:
                right_index -= 1
            start_index = right_index + 1

            word = s[start_index : end_index + 1] if end_index >= 0 else ""
            new_string += (word + " ")
        # Returns a copy of the string with trailing characters removed
        return new_string.rstrip()

#### Method 2 ####
class Solution:
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)

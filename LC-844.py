# https://leetcode.com/problems/backspace-string-compare/description/

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sEdit = []
        tEdit = []

        for char in s: 
            if char == '#': 
                if sEdit: 
                    sEdit.pop()
            else: 
                sEdit += char
        
        for char in t: 
            if char == '#': 
                if tEdit: 
                    tEdit.pop()
            else: 
                tEdit += char

        return sEdit == tEdit

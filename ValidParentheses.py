# https://leetcode.com/problems/valid-parentheses/

class Solution:
    from collections import deque

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s: 
            if char in '({[':
                stack.append(char)
            else: 
                if not stack: 
                    return False
                elif char == ')' and stack[-1] != '(':
                    return False 
                elif char == '}' and stack[-1] != '{':
                    return False                 
                elif char == ']' and stack[-1] != '[':
                    return False 
                stack.pop()
        return not stack 

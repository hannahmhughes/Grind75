# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)

        for x in s: 
            counter[x] += 1

        for x in t: 
            counter[x] -= 1
        
        for value in counter.values(): 
            if value != 0: 
                return False 
        
        return True 
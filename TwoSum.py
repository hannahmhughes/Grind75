class Solution: 
    import List 
    
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        #Use a hash table to store checked complements 
        numMap = {}

        #For each entry in nums, check for complement in hash table. If found, return. If not, add num to table. 
        for i in range(len(nums)): 
            complement = target - nums[i]
            if complement in numMap: 
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []
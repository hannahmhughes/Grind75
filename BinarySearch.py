# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while True: 
            if start > end: 
                return -1

            mid = (start + end) // 2

            if nums[mid] == target: 
                return mid
            elif nums[mid] < target: 
                start = mid + 1
            elif nums[mid] > target: 
                end = mid - 1
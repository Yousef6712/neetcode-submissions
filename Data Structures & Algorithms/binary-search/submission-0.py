class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 
        

        while left <= right:

            indexStart = (left + right) // 2

            if nums[indexStart] == target:
                return indexStart

            elif nums[indexStart] < target:
                left = indexStart + 1 
            
            else:
                right = indexStart - 1

        return -1
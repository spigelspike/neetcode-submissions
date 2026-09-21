""" two pointer method time com, space comp  : O(n log n), O(1) """
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left=0
        right=1
        while right<len(nums):
            if nums[right]==nums[left]:
                return True
            left+=1
            right+=1
        return False
        
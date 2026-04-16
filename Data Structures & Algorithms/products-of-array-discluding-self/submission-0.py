class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
      # Calculate the first (prefix) product
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Calculate the second (suffix) product
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res   
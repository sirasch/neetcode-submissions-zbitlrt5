class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set= set(nums)
        longest_streak=0
        start=0
        for num in num_set:
            if num-1 in num_set:
             continue
            else:
                start=num
            streak=0   
            while start in num_set:
                start+=1
        
                streak+=1

            longest_streak=max(longest_streak, streak)         
        return longest_streak           

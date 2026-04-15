class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for value, freq in count.items():
            buckets[freq].append(value)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for val in buckets[i]:
                result.append(val)
                if len(result) == k:
                    return result
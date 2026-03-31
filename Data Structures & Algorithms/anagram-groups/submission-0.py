class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagroups=defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))   # ('a', 'e', 't')
            anagroups[key].append(s)
        return list(anagroups.values())
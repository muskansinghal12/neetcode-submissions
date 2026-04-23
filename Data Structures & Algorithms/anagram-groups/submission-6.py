class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}
        for s in strs:
            freq = [0]*26
            for i in range(len(s)):
                freq[ord(s[i]) - ord('a')] += 1
            key = tuple(freq)
            if key not in sublists:
                sublists[key] = []
            sublists[key].append(s)
        return list(sublists.values())
            

        
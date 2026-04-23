class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sublists:
                sublists[sorted_s].append(s)
            else:
                sublists[sorted_s] = [s]
        # print(list(sublists.values()))
        return list(sublists.values())
            

        
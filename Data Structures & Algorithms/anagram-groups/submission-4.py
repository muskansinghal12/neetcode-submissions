class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}
        # ans = []
        for word in strs:
            freq = [0]*26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            key = tuple(freq)
            if key not in anagrams_map:
                anagrams_map[key] = []
            anagrams_map[key].append(word)
        
        return list(anagrams_map.values())

        
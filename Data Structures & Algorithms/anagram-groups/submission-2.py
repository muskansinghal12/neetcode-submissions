class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}
        ans = []
        for word in strs:
            new_word = ''.join(sorted(word))
            if new_word in anagrams_map:
                anagrams_map[new_word].append(word)
            else:
                anagrams_map[new_word] = [word]
        for key, value in anagrams_map.items():
            ans.append(value)
        return ans

        
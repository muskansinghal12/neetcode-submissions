from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary = set(wordList)
        queue = deque()
        queue.append((beginWord,1))
        n = len(wordList)
        characters_list = [set() for _ in range(len(beginWord))]
        for i in range(len(beginWord)):
            for word in wordList:
                characters_list[i].add(word[i])
        while queue:
            w, path_len = queue.popleft()
            if w == endWord:
                return path_len
            for i in range(len(beginWord)):
                for c in characters_list[i]:
                    nxt = w[:i]+c+w[i+1:]
                    if nxt in dictionary:
                        dictionary.remove(nxt)
                        queue.append((nxt, path_len+1))
        return 0
        
        


        

        
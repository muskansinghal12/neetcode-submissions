from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary = set(wordList)
        queue = deque()
        queue.append((beginWord,1))
        n = len(wordList)
        while queue:
            w, path_len = queue.popleft()
            if w == endWord:
                return path_len
            for i in range(n):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nxt = w[:i]+c+w[i+1:]
                    if nxt in dictionary:
                        dictionary.remove(nxt)
                        queue.append((nxt, path_len+1))
        return 0
        
        


        

        
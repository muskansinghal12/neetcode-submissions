from collections import deque
class Solution:
    def number_of_matching_chars(self, s1, s2):
        count = 0
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                count += 1
        return count
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append((beginWord,1))
        n = len(wordList)
        current_lengths = [float('inf')]*n
        ans = float('inf')
        visited = [False]*n
        while queue:
            w, path_len = queue.popleft()
            for i in range(n):
                if not visited[i] and self.number_of_matching_chars(w,wordList[i]) == 1:
                    if wordList[i] == endWord:
                        return path_len+1
                    visited[i] = True
                    queue.append((wordList[i],path_len+1))
        return 0
        
        


        

        
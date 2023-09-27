class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #all passed but took too long, may need hashmap
        #try bi-direction bfs some time
        def isWordladder(pre, cur):
            count = 0
            for i in range(len(beginWord)):
                if pre[i] != cur[i]:
                    count += 1
                    if count > 1:
                        return False
            return count == 1

        if endWord not in wordList:
            return 0
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                k = q.popleft()
                for i in wordList:
                    if isWordladder(k, i) and i not in visited:
                        if i == endWord:
                            return res + 1
                        q.append(i)
                        visited.add(i)
        return 0
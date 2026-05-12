import heapq
class Twitter:

    def __init__(self):
        self.time  = 0
        self.tweets = {}
        self.followers = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        # if userId not in self.followers:
        #     return pq
        followers = set()
        if userId in self.followers:
            followers = self.followers[userId].copy()
        followers.add(userId)
        for follower in followers:
            if follower in self.tweets:
                for tweet in self.tweets[follower]:
                    heapq.heappush(pq,tweet)
                    if len(pq) > 10:
                        heapq.heappop(pq)
        ans = []
        while pq:
            ans.append(heapq.heappop(pq)[1])
        return ans[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.followers:
                self.followers[followerId] = set()
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)
        

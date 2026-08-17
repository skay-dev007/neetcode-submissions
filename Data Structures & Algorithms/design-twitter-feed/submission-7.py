# thoughts hashmap and set o(1) loopkups 
# hasmap contains userid and and then everyone they are following as a set 
# How to store posts 
# in a heap, time storing mechanism, so that we know at what time, max heap based on time
#  and then pop 
from collections import defaultdict
import heapq 
class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.count = 0 
        self.users = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # assume tweet id is ordered 
        # so it can use the same 
        self.count += 1 
        self.posts[userId].append((-self.count,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        heapq.heapify(all_tweets)

        
        for follower in self.users[userId] | {userId}:
            for tweet in self.posts[follower]:
                heapq.heappush(all_tweets, tweet)
     

        results = [] 
        
        while len(results) < 10 and all_tweets:

            _, id = heapq.heappop(all_tweets)
            results.append(id)
        
        return results 


    def follow(self, followerId: int, followeeId: int) -> None:

        self.users[followerId].add(followeeId)    

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.users[followerId].discard(followeeId)
        
        

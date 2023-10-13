#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start

import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapping = {}

        for word in words:
            if word not in mapping:
                mapping[word] = 0
            mapping[word] = mapping[word] + 1

        print(mapping)

        heap = []
        for key, value in mapping.items():
            heapq.heappush(heap,Node(key,value))
            if len(heap) >k:
                heapq.heappop(heap)

        res = []
        while len(heap) >0:
            temp = heapq.heappop(heap)
            res.append(temp.key)

        res.reverse()

        return res
class Node:
    def __init__(self,key,value) :
        self.key = key
        self.value = value
    
    def __lt__(self,nxt):
        return self.key > nxt.key if self.value == nxt.value else self.value < nxt.value
# @lc code=end


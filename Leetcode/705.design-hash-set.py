#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        self.hashset = [0]*1000001

    def add(self, key: int) -> None:
        self.hashset[key] = 1

    def remove(self, key: int) -> None:
        self.hashset[key] = 0

    def contains(self, key: int) -> bool:
        return self.hashset[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end


#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if c == ')':
                        if temp != '(':
                            return False
                    if c == ']':
                        if temp != '[':
                            return False
                    if c == '}':
                        if temp != '{':
                            return False
        return True if len(stack) == 0 else False
# @lc code=end


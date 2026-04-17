class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(','}':'{',']':'['}

        for i in s:
            if i not in hashmap:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[i]:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
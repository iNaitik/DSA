class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            elif i == '+':
                k = stack[-2]+stack[-1]
                stack.pop()
                stack.pop()
                stack.append(k)
            elif i == '*':
                k = stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(k)
            elif i == '/':
                k = int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(k)
            elif i == '-':
                k = stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(k)
        return stack[-1]
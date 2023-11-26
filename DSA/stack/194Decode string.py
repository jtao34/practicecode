class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                cur = ''
                while stack[-1] != '[':
                    cur += stack.pop()
                stack.pop() #popout '['
                n = ''
                while stack and stack[-1].isdigit():
                    n += stack.pop()
                n = int(n[::-1])
                #cur = cur[::-1] * n
                stack.append(cur * n)
        return ''.join([word[::-1] for word in stack])
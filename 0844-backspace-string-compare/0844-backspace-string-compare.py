class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def removeBackspaces(s: str) -> [str]:
            stack = []
            for c in s:
                if c == "#" and stack:
                    stack.pop()
                elif c != "#":
                    stack.append(c)
            return stack
        return removeBackspaces(s) == removeBackspaces(t)
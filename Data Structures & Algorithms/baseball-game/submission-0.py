class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            match op:
                case "+":
                    stack.append(int(stack[-1]) + int(stack[-2]))
                    res += int(stack[-1])
                case "C":
                    res -= stack[-1]
                    stack.pop()
                case "D":
                    stack.append(int(stack[-1]) * 2)
                    res += int(stack[-1])
                case _:
                    stack.append(int(op))
                    res += int(stack[-1])
        print(stack)
        return res
        
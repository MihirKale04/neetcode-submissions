class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            print(stack)
            if tokens[i] not in "+-*/":
                stack.append(tokens[i])
            else:
                match tokens[i]:
                    case "+":
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(str(int(num2) + int(num1)))
                    case "-":
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(str(int(num2) - int(num1)))
                    case "*":
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(str(int(num2) * int(num1)))
                    case "/":
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(int(float(num2) / int(num1)))
        return int(stack[0])

        
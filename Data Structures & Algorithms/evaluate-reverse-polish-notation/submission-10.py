class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_list = ['+', '-', '*', '/']
        stack = []
        result = 0
        if not tokens:
            return 0
        elif len(tokens) == 1:
            result = tokens[0]
            return int(result)
        else:
            for token in tokens:
                if token in operator_list:
                    first_num = stack.pop()
                    second_num = stack.pop()
                    if token == '+':
                        result = first_num+second_num
                    elif token == '-':
                        result = second_num-first_num
                    elif token == '*':
                        result = first_num*second_num
                    elif token == '/':
                        result = second_num/first_num
                    stack.append(int(result))
                else:
                    stack.append(int(token))
        return int(result)
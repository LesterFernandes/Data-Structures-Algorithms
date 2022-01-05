def generate_parenthesis(n):
    # only add OPEN parenthesis if open < n
    # only add CLOSE parenthesis if closed < open
    # if open == closed == n - valid result
    stack = []
    rez = []

    def backtrack(openC, closedC):
        if openC == closedC == n:
            rez.append("".join(stack))
            return

        if openC < n:
            stack.append('(')
            backtrack(openC + 1, closedC)
            # print(stack)
            stack.pop()

        if closedC < openC:
            stack.append(')')
            backtrack(openC, closedC + 1)
            # print(stack)
            stack.pop()

    backtrack(0, 0)
    return rez

# print(generateParenthesis(3))

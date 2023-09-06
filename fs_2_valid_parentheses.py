def valid_parentheses(parens):
    stack = []

    parentheses_dict = {')': '('}

    for char in parens:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return len(stack) == 0
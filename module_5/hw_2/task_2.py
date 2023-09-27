def is_balanced(expression):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    expression = input("Enter a sequence of characters: ")
    if is_balanced(expression):
        print("The sequence has balanced brackets.")
    else:
        print("The sequence does not have balanced brackets.")


"""
ChatGPT xD
"""

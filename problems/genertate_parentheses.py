def generate_parentheses(n):

    res = []

    def recursive_parentheses(s, num_open, num_closing):
        if num_open == num_closing == n:
            res.append(s)
        else:
            if num_open < n:
                recursive_parentheses(s + '(', num_open + 1, num_closing)
            if num_closing < num_open:
                recursive_parentheses(s + ')', num_open, num_closing + 1)
        return res

    return recursive_parentheses('', 0, 0)
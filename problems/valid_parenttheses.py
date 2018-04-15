def is_valid(s):
    symbol_list = ['(', '[', '{', ')', ']', '}']
    stack = []
    for symbol in s:
        if symbol in symbol_list[0: 3]:
            stack.append(symbol)
        elif symbol in symbol_list[3: 6]:
            if not stack:
                return False
            else:
                if symbol_list.index(symbol) - symbol_list.index(stack.pop()) != 3:
                    return False
    if stack:
        return False
    else:
        return True

a = "{[]}"
print(is_valid(a))
symbol_list = ['(', '{', '[', ')', '}', ']']
stack = []
for symbol in s:
    if symbol in symbol_list[0: 3]:
        stack.append(symbol)
    elif symbol in symbol_list[3: 6]:
        if not stack:
            return False
        else:
            if symbol_list.index(symbol) - 3 != symbol_list.index(stack.pop()):
                return False
if not stack:
    return True
else:
    return False


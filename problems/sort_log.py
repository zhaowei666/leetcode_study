a = ['b1 9 9 9', 'zoo ok Smart', 'a2 Apple', 'xray ok please']

def reorderElements(logFileSize, logLines):
    words, integers = [], []
    for item in logLines:
        if item.split(' ')[1].isdigit():
            integers.append(item)
        else:
            words.append(item)
    words = sorted(words, compare_log)
    return words + integers


def compare_log(l1, l2):
    space_index = l1.index(' ')
    id1, word1 = l1[: space_index], l1[space_index + 1:]
    space_index = l2.index(' ')
    id2, word2 = l2[: space_index], l2[space_index + 1:]
    if word1 < word2:
        return -1
    elif word1 > word2:
        return 1
    else:
        if id1 < id2:
            return -1
        elif id1 > id2:
            return 1
        else:
            return 0


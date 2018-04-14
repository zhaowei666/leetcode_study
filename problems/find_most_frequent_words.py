import collections

exclude_list = ['a', 'an', 'the', 'and']

a = "Jimmy has an apple, it is on the table. Jimmy likes apple"


def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    words = literatureText.split(' ')
    words = [w for w in words if w not in wordsToExclude]
    word_count = collections.Counter(words)
    res = []
    max_count = 0
    for word in word_count:
        if word_count[word] > max_count:
            res = [word]
            max_count = word_count[word]
        elif word_count[word] == max_count:
            res.append(word)
    return res

a = 'romeo romeo wherefore art thou romeo'
b = ['art' 'thou']

print(retrieveMostFrequentlyUsedWords(a, b))


s = Solution()
print(s.most_frequent_words(a))

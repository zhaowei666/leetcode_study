class Solution(object):
    def length_longest_substring(self, s):
        max_length = 0
        substring = ''
        for letter in s:
            if letter not in substring:
                substring += letter
            else:
                if len(substring) > max_length:
                    max_length = len(substring)
                index_duplicate = substring.index(letter)
                substring = substring[index_duplicate + 1:] + letter
        if len(substring) > max_length:
            max_length = len(substring)
        return max_length

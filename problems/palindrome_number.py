class Solution(object):
    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        for i in range(int(len(str(x)) / 2)):
            if int(x / pow(10, len(str(x)) - i - 1)) % 10 != int(x / pow(10, i) % 10):
                return False
        return True

# Last updated: 5/11/2025, 4:24:26 PM
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ""
        for i in range(len(s)):
            odd = expand_center(i, i)
            even = expand_center(i, i+1)
            longer = odd if len(odd) > len(even) else even
            if len(longer) > len(result):
                result = longer

        return result

            
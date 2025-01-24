class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ""
        
        def expand_around_center(left, right):
            # Expand around the center while it's a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd-length palindromes
            palindrome1 = expand_around_center(i, i)
            # Even-length palindromes
            palindrome2 = expand_around_center(i, i + 1)
            
            # Update the longest palindrome
            longest = max(longest, palindrome1, palindrome2, key=len)
        
        return longest

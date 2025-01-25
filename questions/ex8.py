# itertaive solution 
import re 
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        start = 0
        end = len(s)-1
        if not s or len(s)==1:
            return True 
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True 

# recursive solution 
    def is_palindrome_recursive(s):
        """
        Check if a string is a palindrome using recursion, ignoring spaces, case, and non-alphanumeric characters.
        :param s: str - Input string
        :return: bool - True if the string is a palindrome, False otherwise
        """
        # Preprocess the string: remove non-alphanumeric characters and convert to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        if len(s) <= 1:
            return True

        if s[0] != s[-1]:
            return False

        return is_palindrome_recursive(s[1:-1])

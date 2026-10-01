class Solution:
    def isPalindrome(self, s: str) -> bool:
        return ''.join(c for c in s.upper() if c.isalnum()) == ''.join(c for c in s.upper()[::-1] if c.isalnum())
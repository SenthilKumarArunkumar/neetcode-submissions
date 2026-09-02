class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in range(len(s)):
            if(s[i].isdigit() or s[i].isalpha()):
                res+=s[i]
        return res.lower()==res[::-1].lower()
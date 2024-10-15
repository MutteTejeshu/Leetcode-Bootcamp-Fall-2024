class Solution:
    def reverseWords(self, s: str) -> str:
        # hm = {}
        result = ""
        for index, string in enumerate(reversed(s.split())):
            if index == 0:
                result += string
            else:
                result += " " + string
        
        return result

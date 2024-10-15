class Solution:
    def lengthLastWord(self, s: str) -> int:
        
        endWord = len(s) - 1
        # str em py são iteráveis ==> tratar como um array 
        while s[endWord] == ' ':
            endWord -= 1

        startWord = endWord
        while startWord >= 0 and s[startWord] != ' ':
            startWord -= 1

        return endWord - startWord
        
    def lengthLastWordII(self, s: str) -> int:
        length = 0 
        counting = False 

        for i in s:
            if i != ' ':
                if not counting:
                    counting =  True
                    length = 1
                else:
                    length += 1
            else:
                counting = False

        return length
    
    def lengthLastWordIII(self, s: str) -> int:
        return len(s.split()[-1])







        

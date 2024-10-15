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



        

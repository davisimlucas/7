
class Solution:
    def mergeString(self, word1: str, word2: str):

        x = len(word1)
        y = len(word2)
        i = 0
        j = 0
        result = []

        while i < x or j < y:
            if i < x:
                result.append(word1[i])
                i += 1
            if j < y:
                result.append(word2[j])
                j += 1

        return "".join(result)
    
solution = Solution()

newWord = solution.mergeString('abc', 'pqm')
print(newWord) # output: apbqcm
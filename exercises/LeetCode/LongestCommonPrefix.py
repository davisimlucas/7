class Solution:
    def logestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] #primeira str 
        prefixLen = len(prefix) #size da primeira str

        for s in strs[1:]: #começar pela segunda str
            while prefix != s[0:prefixLen]: 
                prefixLen -= 1
                if prefixLen == 0:
                    return ""
                
                prefix = prefix[0:prefixLen]
        return prefix
class Solution:
    def logestCommonPrefix(self, strs: List[str]) -> str:
        #primeira str 
        prefix = strs[0] 
        #size da primeira str
        prefixLen = len(prefix) 

        #começar pela segunda str até a última 
        for s in strs[1:]: 
            # verificar se a primeira palavra é dif do resto em strs até o tamanho do prefix 
            while prefix != s[0:prefixLen]: 
                # enq for True, diminuir o tamanho palavra que tiver comparando
                prefixLen -= 1
                # se terminar a palavre prefix ==> prefixLen = 0, retornar ""
                if prefixLen == 0:
                    return ""
                #prefix assume o tamanho novo e volta no looping 
                prefix = prefix[0:prefixLen]
        return prefix
class Solution:
    def majorityElement(self, nums: list[int])-> int:
        #dictionary utilizado para contagem de cada elemento em nums
        hash = {}
        #res armazena o elemento majoritário e majoritary a contagem dele em nusm
        res = majority = 0 

        for n in nums:
            #1+hash.get() add 1 ao valor atual ou inicializa caso n tenha aparecido pela 1x  
            hash[n] = 1 + hash.get(n, 0)
            #hash.get() obtem o valor associado a n no dict, se não apareceu ainda na lista, retorna 0
            # se o elem já apareceu, ele retorna 1 unidade em hash[n]
            if hash[n] > majority: 
                # se a contagem n for maior que majority, res assume o valor n e majority assume o novo hash[n]
                res = n
                majority = hash[n]
        return res

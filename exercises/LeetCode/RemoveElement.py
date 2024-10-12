class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        index = 0 # index vai ser a iteração da nova lista formada 

        for i in range(len(nums)):
            if nums[i] != val:
                # se for diferente, ela entrará na lista formada, se for igual não entrará
                nums[index] = nums[i]
                index += 1 #analisar a próxima posição i para o próximo valor válido
        return index
            #OBS: não utilizar a função del() dentro do for looping 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #para casos de array curta de 2 elementos 
        if len(nums)<= 2:
            return len(nums) # retornar a própria array pois terá somente dois elementos mesmo que iguais
        
        k =2 #comparação deve iniciar no terceiro elemento, pois se estiver igual, seria a segunda repetição
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1

        return k
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j = 1 # inicia a contagem em 1 pois para ser igual a alguém é necessário existir algum elemento no i = 0

        for i in range(1, len(nums)): # contador inicia em 1
            if nums[i] != nums[i-1]: #verifica se o i é igual ao anterior 
                nums[j] = nums[i]
                j += 1

        return j 
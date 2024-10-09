class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #para casos de array curta de 2 elementos 
        if len(nums)<= 2:
            return len(nums)
        
        k =2 
        for i in range(1, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k =+ 1

        return k
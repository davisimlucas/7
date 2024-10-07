class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        mIndex = m -1 
        nIndex = n -1 
        result = m + n -1 

        while nIndex >= 0:
            
       
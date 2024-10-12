class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        mIndex = m -1 
        nIndex = n -1 
        result = m + n -1 

        while nIndex >= 0:
            if mIndex >=0 and nums1[mIndex] > nums2[nIndex]:
                nums1[result] = nums1[mIndex]
                mIndex -= 1
            else:
                nums1[result] = nums2[nIndex]
                nIndex -= 1
            
            result -= 1

       
#Merge Sroted Array in Python3

#Approach - 1:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = m-1 
        j = n-1 
        k = m+n-1
        
        while j>=0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
                
#Approach - 2:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        lastElement = m + n - 1  #last index of num1
        
        while m > 0 and n > 0 :  #merge in reverse order
            if nums1[m - 1] > nums2[n - 1]:
                nums1[lastElement] = nums1[m - 1]
                m -= 1
            else:
                nums1[lastElement] = nums2[n - 1]
                n -= 1
            lastElement -= 1
            
            
        while n>0:
            nums1[lastElement] = nums2[n-1]  #filling nums1 with leftover nums2 element
            n -= 1
            lastElement -= 1
        
        
    

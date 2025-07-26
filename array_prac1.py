"""#1 Two sums"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
                
"""#561 Array Partition"""    
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])
        """#217 contains dublicates"""            
 class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums.sort()
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                return True
        return False    
    """#344 Reverse String""" 
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            j=len(s)-1-i
            temp=s[i]
            s[i]=s[j]
            s[j]=temp      
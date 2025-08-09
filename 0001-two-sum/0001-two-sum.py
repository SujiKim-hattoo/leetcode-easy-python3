class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i < j and num1 + num2 == target:
                    ans.append(i)
                    ans.append(j)
        
        return ans

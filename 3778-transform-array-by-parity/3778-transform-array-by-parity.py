class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # Replace each even number with 0 and each odd number with 1.
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
                print(nums)
            else:
                nums[i] = 1
                print(nums)
        
        return sorted(nums)
        
        
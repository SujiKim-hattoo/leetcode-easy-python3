class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}
        
        for i, num in enumerate(nums):
            if num in seen_numbers:
                return [seen_numbers[num], i]
            else:
                new_element = target - num
                seen_numbers[new_element] = i
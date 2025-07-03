class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_op = 0

        for num in nums:
            if num % 3 != 0:  # non divisible by 3
                min_op += 1
        
        return min_op
'''
Intuition: If a number is not divisible by 3, since the remainder when divided by 3 can only be 1 or 2, so only one operation is needed for each such number. 
Approach: Iterate through the list and count how many numbers are not divisible by 3.
Time complexity: O(n) - We iterate through all elements in the list once.
Space complexity: O(1) - We only use a single integer variable(min_op) regardless of input size.
'''            
            
        
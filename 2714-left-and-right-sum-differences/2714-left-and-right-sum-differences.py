class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        rightSum = [0]
        
        # Build cumulative sums from both directions
        for i in range(len(nums) - 1):
            leftSum.append(leftSum[i] + nums[i])
            # rightSum.insert(0, rightSum[-i-1] + nums[-i-1]) -> not good for memory efficiency
            rightSum.append(rightSum[i] + nums[-i-1]) # rightSum will be reversed later
        rightSum.reverse()
        
        # Compute absolute differences between left and right sums
        return [abs(l - r) for l, r in zip(leftSum, rightSum)]
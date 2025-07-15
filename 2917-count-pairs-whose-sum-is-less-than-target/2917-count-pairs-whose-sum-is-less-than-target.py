class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        
        # <third try> _ Memory 17.69MB
        for i in range(len(nums)):
            j = i + 1
            while (j < len(nums)) and (nums[i] + nums[j] < target):
                count += 1
                j += 1
        return count


        # <second try> _ while loop Index Error(out of range)
        # for i in range(len(nums)):
        #     j = i + 1
        #     if j == len(nums):
        #         break
        #     else:
        #         while nums[i] + nums[j] < target:
        #             count += 1
        #             j += 1

        # return count  
        
        # <first try> _ Memory 17.72MB
        # count = 0
         
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (i >= j) or (nums[i] + nums[j] >= target):
        #             continue
        #         else:
        #             count += 1
        
        # return count
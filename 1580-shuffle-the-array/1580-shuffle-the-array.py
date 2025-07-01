class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list = []
        m = n
        for i in range(0, n):
                new_list.append(nums[i])
                new_list.append(nums[m])
                m += 1
        
        return new_list


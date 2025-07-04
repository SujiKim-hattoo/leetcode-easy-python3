class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        double_dict = {}
        double_list = []
        for i in nums:
            if i in double_dict:
                double_dict[i] += 1  # count the occureneces
            else:
                double_dict[i] = 1  # initialize count
        for key, value in double_dict.items():
            if value == 2:
                double_list.append(key)
        
        return sorted(double_list)  
'''
        Intuition: Make a condition loop to find duplicataed numbers.
        Approach: In my first code, I used nested for-loops and if-statements. But it was inefiicient and a bit
        complicated. So I used a dictionary to count occurences instead
        Time complexity: O(n) - Loop through the list and dictionary once. O(2n) -> O(n)
        Space complexity: O(n) - Dictionary and list size depend on input. O(2n) -> O(n)
'''
'''
        My first code:
         double_list = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i < j and nums[i] == nums[j]:
                    if nums[i] not in double_list:
                        double_list.append(nums[i])
        
        return sorted(double_list)
'''
'''
    # Ideal one ...
    from collections import Counter
            
    count = Counter(nums)
    return sorted([num for num, freq in count.items() if freq == 2])
'''
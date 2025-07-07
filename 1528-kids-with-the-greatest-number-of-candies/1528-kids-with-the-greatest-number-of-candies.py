class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        bool_array = []

        for candy in candies:
            if candy + extraCandies >= max_candy:
                bool_array.append(True)
            else:
                bool_array.append(False)
        
        return bool_array
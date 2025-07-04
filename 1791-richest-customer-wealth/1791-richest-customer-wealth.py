class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total_wealth = []
        for customer in accounts:
            total_wealth.append(sum(customer))
        
        return max(total_wealth)

'''
Intuition: Find the maximum total wealth among all customers.
Apporach: Sum each customer's accounts and return the maximum
Time Complexity: O(m * n) - m: number of customers, n: number of banks
Space Complexity: O(m) - storing total wealth for each of m customers
'''

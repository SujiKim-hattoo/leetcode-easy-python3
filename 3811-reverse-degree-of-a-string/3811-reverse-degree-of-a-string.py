class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_rev_dic ={}
        total = 0

        for i in range(len(alphabet_str)):
            alphabet_rev_dic[alphabet_str[i]] = 26 - i

        for i in range(len(s)):
            index_in_rev = alphabet_rev_dic[s[i]]
            index_in_str = i + 1
            total += index_in_rev * index_in_str
        
        return total
            
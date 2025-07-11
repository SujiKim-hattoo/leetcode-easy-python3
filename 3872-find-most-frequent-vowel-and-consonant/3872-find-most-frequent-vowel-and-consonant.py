class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_dic = {}
        consonant_dic = {}
        
        for char in s:
            if char in 'aeiou':  # vowel
                if char not in vowel_dic:
                    vowel_dic[char] = 1
                else:
                    vowel_dic[char] += 1

            else:  # consonant
                if char not in consonant_dic:
                    consonant_dic[char] = 1
                else:
                    consonant_dic[char] += 1

        return max(vowel_dic.values(), default = 0) + max(consonant_dic.values(), default = 0)
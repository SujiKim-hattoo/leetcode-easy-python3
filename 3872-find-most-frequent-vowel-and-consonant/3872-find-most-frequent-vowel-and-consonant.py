class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_dic = {'null': 0}
        consonant_dic = {'null': 0}
        
        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u']:  # vowel
                if char not in vowel_dic:
                    vowel_dic[char] = 1
                    print(vowel_dic)
                else:
                    vowel_dic[char] += 1
                    print(vowel_dic)

            else:  # consonant
                if char not in consonant_dic:
                    consonant_dic[char] = 1
                    print(consonant_dic)

                else:
                    consonant_dic[char] += 1
                    print(consonant_dic)

        return max(vowel_dic.values()) + max(consonant_dic.values())
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_list = list(allowed)
        consistent = 0

        for i in range(0, len(words)):
            each_word = list(words[i])  # e.g., ['a', 'd']
            for j in range(0, len(each_word)):
                if each_word[j] not in allowed_list:
                    break  # exit the inner for loop
                elif j == len(each_word) - 1:
                    consistent += 1

        return consistent

'''
Intuition: Convert the string into a list to allow iteration and comparison.
Approach: Use a nested for loop to iterate over each word and each character in the word. 
          Check if every character is in the allowed list; if not, break out of the loop.
'''

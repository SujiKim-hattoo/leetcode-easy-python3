class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        containing_list = []
        for i in range(0, len(words)):
            if x in words[i]:
                containing_list.append(i)
        
        return containing_list
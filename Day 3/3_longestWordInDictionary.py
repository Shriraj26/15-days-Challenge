"""
Refer to this video for more details!!!
https://www.youtube.com/watch?v=waIgDZZp9Wc
You dont need a Trie for this as it can be solved just using Set
Sort the words, Add them if its prev word exists in the dict 
Then update the result if len is greater
"""


class Solution:
    def longestWord(self, words: List[str]) -> str:

        words.sort()
        result = ""
        mySet = set()
        for word in words:
            if len(word) == 1 or word[:len(word)-1] in mySet:
                mySet.add(word)
                if len(result) < len(word):
                    result = word

        return result

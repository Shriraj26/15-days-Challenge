class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.sentence = ""
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence):
        curr = self.root
        for c in sentence:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
        curr.sentence = sentence

    def search(self, prefix, curr=None):
        if curr == None:
            curr = self.root

        for c in prefix:
            if c not in curr.children:
                return []
            curr = curr.children[c]

        # This list will store our sentences
        ans = []
        for child in curr.children.values():
            if curr.isEnd:
                ans.append(curr.sentence)

            else:
                # Recursively call search method on its children
                # And join it with ans
                ans += self.search("", child)
        print(ans)
        return ans


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.lookup = {}

        # Initialize the dictionary
        for i, sentence in enumerate(sentences):
            self.lookup[sentence] = times[i]

        # Initialize the Trie
        self.trie = Trie()

        # Insert the sentences into the Trie
        for sentence in sentences:
            self.trie.insert(sentence)

        # Store the keyword that is used for search
        self.keyword = ""

    def input(self, c: str) -> List[str]:
        if c == "#":
            # Check if the sentence formed till now exists in the lookup table
            # if yes update its count else init it
            self.lookup[self.keyword] = self.lookup.get(self.keyword, 0) + 1

            # As this is the last sentence, insert it into the Trie
            self.trie.insert(self.keyword)

            # Flush out the keyword
            self.keyword = ""

            # Return the empty list as u wanted for this input
            return []

        else:
            # Add this keyword
            self.keyword += c

            # Get the list
            result = self.trie.search(self.keyword)

            # print the result
            print(result)

            # # Sort and then return the top 3 results
            # result.sort(key = lambda x = (-lookup[x], x))

            return result[:3]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {} #use dict to char and address

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for x in word:
            if x not in node.children:
                node.children[x] = TrieNode()
            node = node.children[x]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for x in word:
            if x not in node.children:
                return False
            node = node.children[x]
        return node.word #True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for x in prefix:
            if x not in node.children:
                return False
            node = node.children[x]
        return True
            
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

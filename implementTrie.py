class Trie(object):

    def __init__(self):
        self.head = {}
        """
        Initialize your data structure here.
        """
        

    def insert(self, word):        
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.head
        for character in word:
            if character not in current:
                current[character] = {}
            current = current[character]
        current['*'] = True            # '*' marks the end of word
        

    def search(self, word):
        current = self.head
        for character in word:
            if character not in current:
                return False
            current = current[character]
        if '*' in current:
            return True
        return False
		
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        current = self.head
        for character in prefix:
            if character not in current:
                return False
            current = current[character]
        return True
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
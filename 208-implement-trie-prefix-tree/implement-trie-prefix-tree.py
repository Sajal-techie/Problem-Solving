class Node:
    def __init__(self):
        self.child = {}
        self.isend = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = Node()
            node = node.child[char]
        node.isend = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.isend

    def startsWith(self, prefix: str) -> bool:
        def helper(node, prefix):
            words = []
            if node.isend:
                words.append(prefix)
            for char, childs in node.child.items():
                words.extend(helper(childs, prefix+char))
            return words
        
        node = self.root
        for char in prefix:
            if char not in node.child:
                return False
            node = node.child[char]
            
        return helper(node,prefix) 
            

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Trie:
    def __init__(self):
        self.child = {}
        self.is_end = False


class Solution:
    def __init__(self):
        self.trie = Trie()
        self.longest = 0
    
    def insert_element(self, word):
        node = self.trie
        for char in word:
            if char not in node.child:
                node.child[char] = Trie()
            node = node.child[char] 
        node.is_end = True
    
    def commonPrefix(self, arr):
        for element in arr:
            curr = 0
            node = self.trie
            for word in str(element):
                if word in node.child:
                    curr += 1
                    node = node.child[word]

                    if self.longest < curr:
                        self.longest = curr
                else:
                    break  

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        for word in arr1:
            self.insert_element(str(word))
        
        self.commonPrefix(arr2)
        return self.longest
    

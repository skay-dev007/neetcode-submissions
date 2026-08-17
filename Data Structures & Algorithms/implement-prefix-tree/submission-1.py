class Node: 
    def __init__(self):
        self.children = {}
        self.ends = False 

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word: 
            if char in node.children: 
                node = node.children[char]
            else: 
                node.children[char] = Node() 
                node = node.children[char]
        node.ends = True 

    def search(self, word: str) -> bool:
        node = self.root 
        for char in word:  
            if char in node.children: 
                node = node.children[char] 
            else: 
                return False 
        if node.ends:
            return True 
        else: 
            return False 
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root 
        for char in prefix: 
            if char in node.children: 
                node = node.children[char] 
            else: 
                return False 
        return True 
        
        
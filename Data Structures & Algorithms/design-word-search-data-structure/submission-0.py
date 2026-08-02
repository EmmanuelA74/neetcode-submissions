class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            curr = node

            for j in range(i, len(word)):
                c = word[j]
                
                #backtrack if char is "." 
                if c == ".":
                    for child in curr.children.values():
                        if dfs(child, j + 1):
                            return True
                        
                    return False
                else:
                    if c not in curr.children:
                        return False
                    
                    curr = curr.children[c]
                
            return curr.endOfWord

        return dfs(self.root, 0)

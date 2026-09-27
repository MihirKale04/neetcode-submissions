class Node:
    def __init__(self, char: str):
        self.val = char
        self.children = []

class PrefixTree:
    def __init__(self):
        self.root = Node('*')

    def insert(self, word: str) -> None:
        word += '?'
        currNode = self.root
        for i in range(len(word)):
            found = False
            for node in currNode.children:
                if node.val == word[i]:
                    currNode = node
                    found = True
                    break
            if not found:
                newNode = Node(word[i])
                currNode.children.append(newNode)
                currNode = newNode

        
    def search(self, word: str) -> bool:
        word += '?'
        currNode = self.root
        for i in range(len(word)):
            found = False
            for node in currNode.children:
                if node.val == word[i]:
                    found = True
                    currNode = node
                    break
            if not found:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for i in range(len(prefix)):
            found = False
            for node in currNode.children:
                if node.val == prefix[i]:
                    found = True
                    currNode = node
                    break
            if not found:
                return False
        return True

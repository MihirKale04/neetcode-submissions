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
                currNode.children.append(Node(word[i]))
                currNode = currNode.children[-1]

        
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
        
        
    
    # {d: {o: {g: {?: {}, g: {y: {?: {}}}}}}}

    # None
    #     -d
    #         -o
    #             -g
    #                 -\0
    #             -\0 
    #     -c
    #         -a
    #             -t
    #                 -\0
    #                 -t
    #                     -l
    #                         -e
    #                             -\0

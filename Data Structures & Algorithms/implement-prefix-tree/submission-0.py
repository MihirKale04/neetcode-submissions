# class Node:
#     def __init__(self, char: str):
#         self.val = char
#         nextChar = []

class PrefixTree:
    def __init__(self):
        self.root = {}


    # i = 0 {d: {}}
    # i = 1 {d: {o : {}}}
    # i = 2 {d: {o : {g: {}}}}
    # end {d: {o : {g: { ?: {}}}}} 

    def insert(self, word: str) -> None:
        level = self.root
        for i in range(len(word)):
            if word[i] in level:
                level = level[word[i]]
            else:
                level[word[i]] = {} 
                level = level[word[i]]
        level['?'] = {}
        
    def search(self, word: str) -> bool:
        word += '?'
        level = self.root
        for i in range(len(word)):
            if word[i] in level:
                level = level[word[i]]
            else:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        level = self.root
        for i in range(len(prefix)):
            if prefix[i] in level:
                level = level[prefix[i]]
            else:
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

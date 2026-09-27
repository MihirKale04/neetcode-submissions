class Solution:    

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            num = len(strs[i])
            res += str(num) + "#" + strs[i]
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        #two state
        #One: find len
        #Two: build str based of len 
        res = []
        State = True
        count = ""
        i = 0
        while i < len(s):
            if State:
                if s[i] == "#":
                    State = False
                else:
                    count += s[i]
                i += 1
            else:
                word = ""
                for j in range((int(count))):
                    word += s[i]
                    i += 1
                res.append(word)
                State = True
                count = ""
        if State:
            return res
        else:
            return [""]
        return res
                


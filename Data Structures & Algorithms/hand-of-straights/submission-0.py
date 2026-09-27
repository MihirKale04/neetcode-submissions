class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Brute Force
            #Scan through each element
            #have this be the "starting" for a group 
                #than scan for consecutive elements and add to grouping
                #until we hit groupSize

                #If we can't find groups that satisfy the condition return False 
        #Questions/Assumptions:
        # -Can we assume that the hand size is divisible by groupSize
        # -The value is an int
        
        #for this implementation I will modify the input hand
        hand.sort()
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1
        while True: #Todo: Figure out condition    
            idx = 0
            while freq[hand[idx]] <= 0:
                idx += 1
                if idx == len(hand):
                    break
            if idx == len(hand):
                break
            firstCardInGroup = hand[idx]
            
            
            
            print ("starting card:", firstCardInGroup)
            for card in range(firstCardInGroup, firstCardInGroup + groupSize):
                if card not in freq or freq[card] <= 0:
                    print("card not in dict")
                    return False
                freq[card] -= 1
                # if freq[card] <= 0:
                #     del freq[card]
        return True
        
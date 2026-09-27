class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #We can use a hash table to store the counts of how many people trust a specific person

        #if we find a person that is trusted by n - 1 people he can potentially be our judge
        #we just need some way to verify that the person has not trusted anybody else.

        #could potentially be over complicating but we can store 2 counts: 
            # 1. how many trust that person
            # 2. how many people does that person trust

        reputation = {}
        trusted = set()
        for truster, trustee in trust: 
            reputation[trustee] = reputation.get(trustee, 0) + 1
            trusted.add(truster)        

        for person, count in reputation.items():
            if count == n - 1:
                #so before we return count we need to verify that the individaul did not trust anybody else
                #to determine that perhaps we can use a set to store individuals who trusted someone. 
                if person not in trusted:
                    return person
        return -1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # this will have a runtime of n
        numberCount = {}
        for num in nums:
            numberCount[num] = numberCount.get(num, 0) + 1
        # --- 

        frequency = [[] for i in range(len(nums) + 1)]

        # this will have a runtime of n
        for num, count in numberCount.items():
            frequency[count].append(num)
        # ---
        print (frequency)

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for number in frequency[i]:
                result.append(number)
                if len(result) == k:
                    return result



        

       



        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1

        while True:
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1
                continue
            if numbers[index1] + numbers[index2] < target:
                index1 += 1
                continue 
            if numbers[index1] + numbers[index2] == target:
                return [index1 + 1, index2 + 1]
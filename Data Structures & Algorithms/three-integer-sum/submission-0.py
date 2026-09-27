class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):  # Iterate up to the third-to-last element
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate starting numbers
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate numbers for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1  # Move pointers regardless of duplicates (after handling them)
                    right -= 1

                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return ans



        
        
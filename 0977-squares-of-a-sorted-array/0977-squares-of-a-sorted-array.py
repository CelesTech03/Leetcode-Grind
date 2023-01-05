class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        sortedArr = [0 for _ in nums]

        smallerValueIdx = 0
        largerValueIdx = len(nums) - 1

        # Looping from right to left (last index to first)
        for idx in reversed(range(len(nums))):
            smallerValue = nums[smallerValueIdx]
            largerValue = nums[largerValueIdx]

            if abs(smallerValue) > abs(largerValue):
                sortedArr[idx] = smallerValue * smallerValue
                smallerValueIdx += 1
            else:
                sortedArr[idx] = largerValue * largerValue
                largerValueIdx -= 1

        return sortedArr
        # O(n) time | O(n) space
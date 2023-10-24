from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return low



    


solution = Solution()
nums = [1, 3, 5, 6]
ans = solution.searchInsert(nums=nums, target=9)
print(ans)
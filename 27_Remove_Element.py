


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i  in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"

        print(nums)


solution = Solution()
solution.removeElement([3, 4, 3, 4, 5], 3)
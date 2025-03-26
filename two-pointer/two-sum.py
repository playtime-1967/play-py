class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        store = {}
        for (i, num) in enumerate(nums):
            num2 = target - num
            if num2 in store:
                return [store[num2], i]
            store[num] = i

        return [-1, -1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        pivot = 0
        suma = 0

        for n in range(0, len(nums)):
            for i in range(n+1, len(nums)):
                if (nums[n] + nums[i]) == target:
                    return [n, i]
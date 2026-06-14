class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for i in range(len(nums)):
            if nums[i] in x:
                return True
            else:
                x.add(nums[i])
        return False
        
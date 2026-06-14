class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1
        while lp <= rp:
            mp = (lp + rp) // 2
            print(lp, rp, mp)
            if nums[mp] == target:
                return mp
            if nums[mp] > target:
                rp = mp -1
            else:
                lp = mp + 1
        return -1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {i:[] for i in nums}
        for i in range(len(nums)):
            hashMap[nums[i]].append(i)
        print(hashMap)

        for i in range(len(nums)):
            print(nums[i], hashMap)
            current_num = target - nums[i]
            if current_num in hashMap.keys():
                for j in range(len(hashMap[current_num])):
                    if hashMap[current_num][j] != i:
                        return [i, hashMap[current_num][j]]
        
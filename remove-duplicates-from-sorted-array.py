class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(0, len(nums) - 1):
            i = i - j
            if nums[i] == nums[i+1]:
                nums.pop(i)
                j+=1

        return len(nums)
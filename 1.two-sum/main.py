class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            search = target - num
            if search in num_map:
                return [num_map[search], i]
            num_map[num] = i
        return []
        

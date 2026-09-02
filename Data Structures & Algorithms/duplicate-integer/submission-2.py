class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_array = set()
        for num in nums:
            if num in distinct_array:
                return True
            distinct_array.add(num)
        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setty = set()
        for num in nums:
            if num in setty:
                return True
            elif num not in setty:
                setty.add(num)
        return False



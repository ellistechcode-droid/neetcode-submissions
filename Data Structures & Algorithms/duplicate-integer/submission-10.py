class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seto = set()

        for num in nums:
            if num in seto:
                return True
            elif num not in seto:
                seto.add(num)
        return False



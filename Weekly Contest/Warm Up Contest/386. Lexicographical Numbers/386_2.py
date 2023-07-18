class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(x) for x in range(1, n + 1)]
        nums.sort()
        return [int (x) for x in nums]
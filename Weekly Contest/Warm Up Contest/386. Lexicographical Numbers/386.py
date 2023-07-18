class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num = 1
        res = list()
        for i in range(n):
            res.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num == n or num % 10 == 9:
                    num //= 10
                num += 1
        return res
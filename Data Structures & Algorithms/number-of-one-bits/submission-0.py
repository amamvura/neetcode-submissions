class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n != 0:
            answer += 1
            n = n & (n-1)
        return answer



        
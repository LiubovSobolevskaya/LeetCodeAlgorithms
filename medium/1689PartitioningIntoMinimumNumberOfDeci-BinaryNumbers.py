class Solution:
    def minPartitions(self, n: str) -> int:
        maxDigit = 0
        for i in range(0, len(n)):
            if int(n[i]) > maxDigit:
                maxDigit = int(n[i])
        return maxDigit
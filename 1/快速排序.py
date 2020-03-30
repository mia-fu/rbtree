class Solution(object):
    def insertionSort(self, a, n):
        if n <= 1:
            return
        for i in range(n):
            print i


if __name__ == "__name__":
    s = Solution()
    print s.insertionSort([1, 2, 4], 3)

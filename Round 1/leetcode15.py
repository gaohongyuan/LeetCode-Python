# 3Sum

# TLE if using the method in Subset II.

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        res = []
        comb = self.genComb(l, 3)
        for case in comb:
            subset = []
            for digit in case:
                subset.append(nums[digit - 1])
            if sum(subset) == 0 and not subset in res:
                res.append(subset)
        return res

    def genComb(self, n, k):
        a = range(1, k + 1)
        res = []
        while True:
            cur = k - 1
            while a[cur] <= n:
                res.append(a[:])
                a[cur] += 1
            while a[cur] > n - k + cur:
                cur -= 1
                if cur < 0:
                    return res
            a[cur] += 1
            for i in range(cur + 1, k):
                a[i] = a[cur] + i - cur

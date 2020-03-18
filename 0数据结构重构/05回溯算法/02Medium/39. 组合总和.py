import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res_set = [[]]
        item = []

        self.helper(0, candidates, item, res_set, target, 0)

        return res_set

    def helper(self, i, candidates, item, res_set, target, sum):
        if i >= len(item) or sum > target:
            return
        sum += candidates[i]
        item.append(copy.deepcopy(candidates[i]))

        if target == sum:
            
            res_set.append(copy.deepcopy(item))




if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    s.combinationSum(candidates, target)

    """
    所求解集为:
[
  [7],
  [2,2,3]
]
    """
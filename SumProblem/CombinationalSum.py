"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        ret = []
        self.dfs(sorted(candidates), target, 0, [], ret)
        return ret
    
    def dfs(self, nums, target, idx, path, ret):
        if target <= 0:
            if target == 0:
                ret.append(path)
            return 
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)

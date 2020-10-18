def fourSum(self, nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[List[int]]
  """
  nums.sort()
  N, result = len(nums), []
  for i in range(N):
      if i > 0 and nums[i] == nums[i-1]:
          continue
      for j in range(i+1, N):
          if j > i+1 and nums[j] == nums[j-1]:
              continue
          x = target - nums[i] - nums[j]
          s,e = j+1, N-1
          while s < e:
              if nums[s]+nums[e] == x:
                  result.append([nums[i], nums[j], nums[s], nums[e]])
                  s = s+1
                  while s < e and nums[s] == nums[s-1]:
                      s = s+1
              elif nums[s]+nums[e] < x:
                  s = s+1
              else:
                  e = e-1
  return result

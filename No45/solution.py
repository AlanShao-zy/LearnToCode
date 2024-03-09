from typing import List


# leetcode solution

'''
    t[i] = min step of i
    t[i+1] = min([t[j] for j in range(i+1) if j + l[j] >= i+1]) + 1

'''

class Solution:
    def jump_1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        steps = []
        for i in range(n):
            if i == 0:
                steps.append(0)
            else:
                min_step = n + 1
                for j in range(i):
                    if j + nums[j] >= i:
                        min_step = min(min_step, steps[j])
                steps.append(min_step+1)
        print(steps)
        return steps[-1]

    def jump_2(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        min_step = 0
        cur_max_len = 0
        next_max_len = 0
        n = len(nums)

        for i in range(n):
            next_max_len = max(next_max_len, i+nums[i])
            if next_max_len >= n-1:
                return min_step + 1
            if i == cur_max_len:
                min_step += 1
                cur_max_len = next_max_len

        return None   


def main():
    nums = [3,1,3,1,4]
    print(Solution().jump(nums))


if __name__ == "__main__":
    main()
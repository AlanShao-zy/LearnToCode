## 最简单-动态规划
记t(i)为走到数组i位置时的最小步数
那么可以得到
t(i+1) = min([t(j) for j in range(i+1) if j+nums[j]>=i+1]) + 1

时间：O(n)
空间：O(n)

## 进阶
首先观察到t(i)是单调递增的，证明：假设到i的最短路径，前一跳为j
1. 如果j=i-1，可得t(i)>t(i-1)
2. 如果j<i-1, 此时可得t(i)=t(i-1)
证毕

因此，只需要维护一个min_step，判断什么时候加min_step即可
每一步都有一个最长的步长，超出步长范围则必须走下一步

cur_max_len
next_max_len

next_max_len = max(next_max_len, i + nums[i])

if i == cur_max_len:
    cur_max_len = next_max_len
    step += 1

if next_max_len >= n-1: return min_step+1

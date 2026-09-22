"""
LeetCode 169. 多数元素（简单）
https://leetcode.cn/problems/majority-element/

题目：数组里有一个元素出现的次数超过数组长度的一半，找出这个元素。
      （可以假设数组非空，且多数元素一定存在）

思路：和 136 同一个套路 —— 判断「出现次数超过一半」，
      同样得先知道「各出现了几次」，所以还是用字典计数。
      第一遍：数次数（和 136 一模一样）
      第二遍：找出「次数 > len(nums) / 2」的那一项

      因为题目保证多数元素一定存在，所以也有个更省事的写法：
          return max(count, key=count.get)
      出现次数最多的那个必然是答案，不用自己判断一半。

复杂度：时间 O(n)，空间 O(n)

易错点：
      1. 条件是「超过一半」= v > len(nums) / 2。
         写成 v > len(nums) 永远不会成立（次数不可能超过数组总长度），
         而且不会报错，只是静静返回 None —— 这种最不好查
      2. 第二个 for 要和第一个 for 平级，别不小心缩进到里面去
"""


def majorityElement(nums):
    count = {}
    for x in nums:
        count[x] = count.get(x, 0) + 1
    for k, v in count.items():
        if v > len(nums) / 2:
            return k


if __name__ == "__main__":
    cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
    ]
    for nums, expected in cases:
        result = majorityElement(nums)
        ok = result == expected
        print(f"[{'通过' if ok else '不通过'}] {nums} -> {result}，期望 {expected}")
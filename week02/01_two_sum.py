"""
LeetCode 1. 两数之和（简单）
https://leetcode.cn/problems/two-sum/

题目：给定一个整数数组 nums 和一个整数目标值 target，
      找出数组中和为 target 的那两个数，返回它们的下标。
      每个输入只会对应一个答案，同一个元素不能重复使用。

思路：（先用中文把你的想法写在这里）


复杂度：时间 O(n²)，空间 O(1)

提示：先用双重循环写出来，这就是你在第 1 周卡住的那道题。
      这周会学字典，学完之后想想怎么用字典把时间降到 O(n)：
      一边遍历，一边把「已经见过的数字 -> 它的下标」存进字典。
      关键问题：遍历到 nums[i] 时，你要找的「另一个数」是多少？
               用 target 减去它就能算出来。
"""


def twoSum(nums, target):
    # TODO: 在这里写你的代码
    pass


if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for nums, target, expected in cases:
        result = twoSum(nums, target)
        ok = result is not None and sorted(result) == sorted(expected)
        print(f"[{'通过' if ok else '不通过'}] nums={nums}, target={target} -> {result}，期望 {expected}")
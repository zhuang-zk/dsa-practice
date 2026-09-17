"""
LeetCode 26. 删除有序数组中的重复项（简单）
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

题目：给你一个非严格递增排列的数组 nums，原地删除重复元素，
      使每个元素只出现一次，返回删除后数组的新长度。

思路：（先用中文把你的想法写在这里）


复杂度：时间 O(n)，空间 O(1)

提示：数组已经有序，重复元素一定挨在一起。还是快慢指针：
      fast 找"和 slow 位置的值不一样"的元素，找到就搬到 slow 的下一位。
"""


def removeDuplicates(nums):
    # TODO: 在这里写你的代码
    pass


if __name__ == "__main__":
    cases = [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
    ]
    for nums, kept in cases:
        result = removeDuplicates(nums)
        ok = result == len(kept) and nums[:result] == kept
        print(f"[{'通过' if ok else '不通过'}] 输入 {nums} → 返回 {result}，期望 {len(kept)}")
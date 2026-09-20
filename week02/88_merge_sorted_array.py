"""
LeetCode 88. 合并两个有序数组（简单）
https://leetcode.cn/problems/merge-sorted-array/

题目：nums1 和 nums2 都是非递减排列的整数数组。
      nums1 的长度是 m + n，前 m 个是有效数据，后 n 个是占位的 0。
      nums2 的长度是 n。
      要求把 nums2 合并进 nums1，让 nums1 变成有序数组，原地修改，不返回东西。

思路：（先用中文把你的想法写在这里）


复杂度：时间 O(m + n)，空间 O(1)

提示：如果从前往后合并，会把 nums1 里还没处理的数据覆盖掉。
      所以试试从后往前：谁的末尾大，就把谁放到 nums1 的最后。
      三个指针：
        i 指向 nums1 的有效数据末尾（下标 m - 1）
        j 指向 nums2 的末尾（下标 n - 1）
        k 指向 nums1 的最后一个位置（下标 m + n - 1）
      注意 nums2 先走完的情况不用管，nums1 剩下的本来就在原位。
"""


def merge(nums1, m, nums2, n):
    # TODO: 在这里写你的代码
    pass


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]
    for nums1, m, nums2, n, expected in cases:
        merge(nums1, m, nums2, n)
        ok = nums1 == expected
        print(f"[{'通过' if ok else '不通过'}] m={m}, nums2={nums2}, n={n} -> {nums1}，期望 {expected}")
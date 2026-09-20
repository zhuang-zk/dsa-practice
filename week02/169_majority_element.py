"""
LeetCode 169. 多数元素（简单）
https://leetcode.cn/problems/majority-element/

题目：数组里有一个元素出现的次数超过数组长度的一半，找出这个元素。
      （可以假设数组非空，且多数元素一定存在）

思路：（先用中文把你的想法在这里写出来）


复杂度：时间 O(n)，空间 O(n)（用字典）；进阶解法能做到空间 O(1)

提示：最容易想到的做法——用字典统计每个数字出现的次数，
      然后找出出现次数最多的那个。
      做完可以想想：有没有办法只扫一遍、还不用额外的字典？
      （有个叫「摩尔投票」的解法，思路是「不同就互相抵消」，做完了再看。）
"""


def majorityElement(nums):
    # TODO: 在这里写你的代码
    pass


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
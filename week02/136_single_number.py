"""
LeetCode 136. 只出现一次的数字（简单）
https://leetcode.cn/problems/single-number/

题目：数组中除了某个元素只出现一次，其余元素都出现两次。
      找出那个只出现一次的元素，要求时间 O(n)、空间 O(1)。

思路：（先用中文把你的想法写在这里）


复杂度：时间 O(n)，空间 O(1)（用字典的话空间是 O(n)，进阶解法才是 O(1)）

提示：先用这周学的字典做——遍历一遍，统计每个数字出现了几次，
      最后找出出现 1 次的那个。这是最容易想通的做法，先把它写出来。
      做完再想想：有没有办法不用额外的字典？
      （提示：考虑位运算里的「异或」，a ^ a = 0，a ^ 0 = a。想不通就跳过，后面会学。）
"""


def singleNumber(nums):
    # TODO: 在这里写你的代码
    pass


if __name__ == "__main__":
    cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ]
    for nums, expected in cases:
        result = singleNumber(nums)
        ok = result == expected
        print(f"[{'通过' if ok else '不通过'}] {nums} -> {result}，期望 {expected}")
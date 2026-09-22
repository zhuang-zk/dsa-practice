"""
LeetCode 136. 只出现一次的数字（简单）
https://leetcode.cn/problems/single-number/

题目：数组中除了某个元素只出现一次，其余元素都出现两次。
      找出那个只出现一次的元素。

思路：题目要判断「只出现一次」，就得先知道「出现了几次」。
      而数组本身不携带次数信息，所以自己建一个记录本 ——
      字典：数字 -> 出现次数。
      两遍扫描：
        第一遍：数次数，核心一行 count[x] = count.get(x, 0) + 1
        第二遍：遍历字典，找出次数为 1 的那一项，返回它的键

复杂度：时间 O(n)，空间 O(n)

易错点：
      1. for k, v in count.items() 里，v 本身已经是次数了，
         直接 if v == 1 就行，不用再 count[...] 去查一遍
      2. 给变量加引号会变成字符串（'v' 是字母 v，不是变量 v）
      3. 要返回的是键 k（数字本身），不是值 v（次数）
"""


def singleNumber(nums):
    count = {}
    for x in nums:
        count[x] = count.get(x, 0) + 1
    for k, v in count.items():
        if v == 1:
            return k


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
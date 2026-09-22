"""
集合基础：交集、并集这些怎么用
运行：python drill/set_basics.py

集合（set）= 一堆不重复、没有顺序的元素。
写法：{1, 2, 3}
筛选用途：快速判断「在不在」（比列表快得多），以及做集合运算。
"""

print("=" * 54)
print("第 1 部分：四个基本运算")
print("=" * 54)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"a = {a}")
print(f"b = {b}")
print()
print(f"a & b = {a & b}      交集：两个都有的")
print(f"a | b = {a | b}  并集：合起来，重复只留一个")
print(f"a - b = {a - b}      差集：a 有、b 没有的")
print(f"a ^ b = {a ^ b}  对称差：只出现在一个里的")

print()
print("=" * 54)
print("第 2 部分：实际用法（谁在两个班都出现）")
print("=" * 54)
ban1 = {"小明", "小红", "小刚"}
ban2 = {"小红", "小刚", "小美"}
print(f"一班：{ban1}")
print(f"二班：{ban2}")
print(f"两个班都有：{ban1 & ban2}")
print(f"合起来所有同学：{ban1 | ban2}")
print(f"只在一班、不在二班：{ban1 - ban2}")
print("（注意：集合没有顺序，打印出来的排列每次可能不一样）")

print()
print("=" * 54)
print("第 3 部分：力扣 349 两个数组的交集")
print("=" * 54)
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(f"nums1 = {nums1}  ->  set(nums1) = {set(nums1)}")
print(f"nums2 = {nums2}          ->  set(nums2) = {set(nums2)}")
print(f"set(nums1) & set(nums2) = {set(nums1) & set(nums2)}   <- 就是答案")

print()
print("=" * 54)
print("第 4 部分：列表不能直接用 &")
print("=" * 54)
try:
    r = [1, 2] & [2, 3]
except TypeError as e:
    print(f"列表直接用 & 会报错：{e}")
print(f"要先转成集合：{set([1, 2]) & set([2, 3])}")
print("力扣要求返回列表，就再套一层 list()：")
print(f"list(set([1, 2]) & set([2, 3])) = {list(set([1, 2]) & set([2, 3]))}")

print()
print("=" * 54)
print("最容易忘的一点：判断「在不在」用集合更快")
print("=" * 54)
lst = [1, 2, 3, 4, 5]
st = {1, 2, 3, 4, 5}
print(f"3 in {lst}  ->  {3 in lst}      （列表要一个一个找）")
print(f"3 in {st}   ->  {3 in st}       （集合一步到位）")
print("数据量大时差距非常明显，这就是哈希表的作用。")
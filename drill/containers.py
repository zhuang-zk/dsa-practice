"""
第 2 周基础知识：Python 四种容器
运行：python drill/containers.py

    列表 list    [1, 2, 3]     有序、可改、可以有重复
    元组 tuple   (1, 2, 3)     有序、不可改、可以有重复
    字典 dict    {"a": 1}      键值对、可改、键不重复
    集合 set     {1, 2, 3}     无序、可改、自动去重
"""

print("=" * 54)
print("第 1 部分：列表 list —— 刷题最常用")
print("=" * 54)

nums = [5, 5, 1]
print(f"初始：{nums}")

nums.append(5)
print(f"append(5)      末尾加一个     -> {nums}")

nums.insert(0, 9)
print(f"insert(0, 9)   在下标 0 插入  -> {nums}")

nums.remove(9)
print(f"remove(9)      删掉值 9       -> {nums}")

last = nums.pop()
print(f"pop()          弹出末尾 {last}  -> {nums}")

nums.sort()
print(f"sort()         原地排序       -> {nums}")

print()
print(f"len(nums)  取长度   -> {len(nums)}")
print(f"sum(nums)  求和     -> {sum(nums)}")
print(f"max(nums)  最大值   -> {max(nums)}")
print(f"min(nums)  最小值   -> {min(nums)}")
print(f"5 in nums  在不在   -> {5 in nums}")
print(f"nums[0]    取第 0 个 -> {nums[0]}")
print(f"nums[-1]   取最后一个 -> {nums[-1]}")
print(f"nums[1:3]  切片（下标 1 到 2，不含 3）-> {nums[1:3]}")
print(nums[0:5])

print()
print("  二维列表（杨辉三角用的就是它）：")
grid = [[1, 2], [3, 4]]
print(f"    grid = {grid}")
print(f"    grid[1][0] -> {grid[1][0]}   （先取第 1 行，再取那一行的第 0 个）")

print()
print("=" * 54)
print("第 2 部分：元组 tuple —— 不能改的列表")
print("=" * 54)

point = (3, 5)
print(f"point = {point}")
print(f"point[0] 能取  -> {point[0]}")
print(f"len(point) -> {len(point)}")
try:
    point[0] = 99
except TypeError as e:
    print(f"point[0] = 99 会报错 -> TypeError: {e}")

x, y = point
print(f"拆包：x, y = point  ->  x={x}, y={y}")

print()
print("  什么时候用元组？")
print("    1. 数据不该被改动时（比如坐标、配置）")
print("    2. 函数要返回多个值：return 最小值, 最大值")

print()
print("=" * 54)
print("第 3 部分：集合 set —— 自动去重 + 快速查找")
print("=" * 54)

s = {1, 2, 2, 3, 3, 3}
print(f"{{1, 2, 2, 3, 3, 3}}  自动去重 -> {s}")

s.add(4)
print(f"add(4)        -> {s}")
s.remove(1)
print(f"remove(1)     -> {s}")
print(f"3 in s        -> {3 in s}   （比在列表里找快得多）")
print(len(s))

print()
print("  集合还能做数学运算：")
a = {1, 2, 3}
b = {2, 3, 4}
print(f"    a = {a}   b = {b}")
print(f"    a & b  交集（两边都有）  -> {a & b}")
print(f"    a | b  并集（合起来）    -> {a | b}")
print(f"    a - b  差集（a 有 b 没有）-> {a - b}")

print()
print(f"  去重最简写法：list(set([1, 2, 2, 3])) -> {list(set([1, 2, 2, 3]))}")
print("  注意：集合是无序的，不能按下标取，s[0] 会报错")
try:
    s[0]
except TypeError as e:
    print(f"    s[0] -> TypeError: {e}")

print()
print("=" * 54)
print("第 4 部分：四种容器怎么选")
print("=" * 54)
print("""
    要按下标取第几个      -> 列表 / 元组
    要频繁增删改          -> 列表
    数据不该被改          -> 元组
    要「甲 -> 乙」的对应  -> 字典
    要「每个东西出现几次」-> 字典（值放次数）
    要去重 / 判断在不在   -> 集合
    要数学上的交并差      -> 集合
""")
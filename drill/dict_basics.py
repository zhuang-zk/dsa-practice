"""
字典基础：刷题最常用的 5 个操作
运行：python drill/dict_basics.py

字典 = 一堆「键 -> 值」的对应关系。
    键（key）：用来查的
    值（value）：查出来的东西
写法：{键1: 值1, 键2: 值2}
"""

print("=" * 52)
print("第 1 步：字典长什么样")
print("=" * 52)

student = {"name": "小庄", "age": 18, "major": "车辆工程"}
print(f"整个字典：{student}")
print(f"student['name']  ->  {student['name']}")
print(f"student['age']   ->  {student['age']}")

print()
print("=" * 52)
print("第 2 步：增、改、查")
print("=" * 52)

d = {}
d["a"] = 1
print(f"d['a'] = 1   ->  {d}   （键不存在 = 新增）")
d["a"] = 99
print(f"d['a'] = 99  ->  {d}   （键已存在 = 覆盖）")
print(f"d['a']       ->  {d['a']}")

print()
print("=" * 52)
print("第 3 步：键在不在？用 in")
print("=" * 52)

d = {"a": 1}
print(f"'a' in d  ->  {'a' in d}")
print(f"'b' in d  ->  {'b' in d}")
try:
    d["b"]
except KeyError as e:
    print(f"直接取不存在的键会报错：KeyError: {e}")

print()
print("=" * 52)
print("第 4 步：计数套路（刷题最常用！）")
print("=" * 52)

nums = [2, 2, 1, 4, 1, 2]
print(f"要数的数组：{nums}")

count = {}
for x in nums:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
print(f"写法一（先判断）：{count}")

count2 = {}
for x in nums:
    count2[x] = count2.get(x, 0) + 1
print(f"写法二（用 get）：{count2}")

print()
print("  get(x, 0) 的意思是：x 在字典里就返回它的值，不在就返回 0。")
print("  所以 count[x] = count.get(x, 0) + 1 这一行，")
print("  等价于「把 x 的次数加一，没见过就当 0 开始加」。")

print()
print("=" * 52)
print("第 5 步：遍历字典")
print("=" * 52)

d = {"a": 3, "b": 7, "c": 1}
print("只拿键：")
for k in d:
    print(f"    {k}  ->  {d[k]}")
print("同时拿键和值：")
for k, v in d.items():
    print(f"    {k}  ->  {v}")

print()
print("=" * 52)
print("第 6 步：找出「值最大」的那个键")
print("=" * 52)

d = {"a": 3, "b": 7, "c": 1}
print(f"字典：{d}")
print(f"max(d, key=d.get)  ->  {max(d, key=d.get)}   （意思是：按值来比大小，返回对应的键）")

print()
print("=" * 52)
print("第 7 步：实战——136 题的骨架")
print("=" * 52)

nums = [2, 2, 1, 4, 1, 2]
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
print(f"先把次数数出来：{count}")
print("接下来只要遍历这个字典，找出值为 1 的那个键，就是答案。")
for k, v in count.items():
    if v == 1:
        print(f"    {k} 只出现了 1 次 -> 答案就是它")
"""
元组 tuple 进阶：它的「不可变」是浅层的
运行：python drill/tuple_basics.py

    列表 list  = 敞口筐，随时能往里扔东西
    元组 tuple = 焊死的储物柜，格子数量、每格装哪个筐，全焊死了
                 但格子里的筐还是敞口筐 —— 照样能往里扔东西
"""

print("=" * 54)
print("第 1 部分：元组不挑食，什么都能装")
print("=" * 54)

t = (1, "abc", [1, 2], {"a": 1}, (3, 4))
print(f"t = {t}")
print(f"len(t) = {len(t)}")
print(f"t[0] -> {t[0]}     第 0 格：整数")
print(f"t[2] -> {t[2]}     第 2 格：列表")
print(f"t[3] -> {t[3]}     第 3 格：字典")
print(f"t[4] -> {t[4]}     第 4 格：另一个元组")
print()
print("  元组只是一排「固定长度的格子」，每格里放什么都行。")
print("  所以「元组里为什么有列表」的答案是：因为你可以放。")

print()
print("=" * 54)
print("第 2 部分：焊死的部分 —— 格子本身")
print("=" * 54)

point = (3, 5)
print(f"point = {point}")
print(f"取值没问题：point[0] -> {point[0]}")
try:
    point[0] = 99
except TypeError as e:
    print(f"想换掉格子里的东西 -> TypeError: {e}")
print()
print("  报错措辞是 'does not support item assignment'（不支持给格子赋值），")
print("  管的是「第 0 格指向谁」，不是「第 0 格里的东西长什么样」。")

print()
print("=" * 54)
print("第 3 部分：坑 —— 元组里装列表，照样能改")
print("=" * 54)

t2 = ([1, 2], (3, 4))
print(f"初始：{t2}")
print(f"id(t2[0]) = {id(t2[0])}   （先记住这个地址）")

t2[0].append(99)
print(f"执行 t2[0].append(99) 之后：{t2}")
print(f"id(t2[0]) = {id(t2[0])}   （地址没变，筐还是那个筐）")
print()
print("  元组一个格子都没动，动的是格子里的那个列表。")
print("  「元组不可变」= 格子焊死，不等于「里面的东西冻住」。")

print()
print("=" * 54)
print("第 4 部分：三个动作，三种结果")
print("=" * 54)

t3 = ([1, 2], (3, 4))
print(f"t3 = {t3}")
print()
print("  动作 1：t3[0].append(99)   改列表自己")
t3[0].append(99)
print(f"      -> {t3}   成功")
print()
print("  动作 2：t3[0] = [7, 8]     想换掉第 0 格")
try:
    t3[0] = [7, 8]
except TypeError as e:
    print(f"      -> TypeError: {e}")
print()
print("  动作 3：t3[1].append(5)    第 1 格本来就是元组")
try:
    t3[1].append(5)
except AttributeError as e:
    print(f"      -> AttributeError: {e}")

print()
print("""
    对照表：
        t3[0].append(99)    成功            动的是筐，不是柜子
        t3[0] = [7, 8]      TypeError       想换柜子里的东西，柜子是焊死的
        t3[1].append(5)     AttributeError  这一格本来就是元组，没有 append
""")

print("=" * 54)
print("第 5 部分：想真的一点都改不了 -> 元组套元组")
print("=" * 54)

safe = ((1, 2), (3, 4))
print(f"safe = {safe}")
try:
    safe[0].append(99)
except AttributeError as e:
    print(f"safe[0].append(99) -> AttributeError: {e}")
print("  里外都是元组，这才叫真的只读。")

print()
print("=" * 54)
print("第 6 部分：顺带讲清 += —— 那不是「改」，是「换了个新的」")
print("=" * 54)

t = (1, 2)
print(f"元组  t = {t}    id = {id(t)}")
t += (3,)
print(f"t += (3,) 之后  t = {t}    id = {id(t)}")
print("  id 变了！说明元组没被修改，而是新造了一个 (1, 2, 3)，变量 t 改成指过去。")
print()
lst = [1, 2]
print(f"列表  lst = {lst}    id = {id(lst)}")
lst += [3]
print(f"lst += [3] 之后  lst = {lst}    id = {id(lst)}")
print("  列表的 id 没变：真的是在原地加东西。对比一下就懂了。")

print()
print("=" * 54)
print("第 7 部分：和刷题直接相关的一条")
print("=" * 54)
print("  元组里装了列表，就不能当集合元素、也不能当字典的键：")
try:
    bad = {([1, 2], 3)}
except TypeError as e:
    print(f"     -> TypeError: {e}")
print("  因为集合和字典的键都要求「不可变」，而它里面藏着能改的列表，")
print("  Python 干脆拒绝。想用就全换成元组：")
good = {((1, 2), 3)}
print(f"     {((1, 2), 3)} 放进集合 -> {good}   可以")

print()
print("=" * 54)
print("一句话总结")
print("=" * 54)
print("""
    元组不可变  ≠  里面的东西不可变
    元组管的是「格子」：一共几格、每格指向谁
    格子里的东西能不能变，归它自己的类型管：
        整数、字符串、元组  -> 本来就改不了
        列表、字典、集合    -> 该改还是能改
""")
def f(data):
    print("刚进函数时   : data is x ->", data is x)
    data = [1, 2, 3]
    print("执行 data = [1,2,3] 之后: data is x ->", data is x)
    print("                          data 的 id =", id(data), " x 的 id =", id(x))
    data.append(4)
    print("再 append(4) 之后: 函数里的 data =", data)

x = [9, 9]
print("调用前 x =", x, " id =", id(x))
f(x)
print("调用后 x =", x, " id =", id(x))
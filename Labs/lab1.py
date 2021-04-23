from sympy import *
x = Symbol('x')


# 输入区间范围[start_x, end_x]和等分次数n，返回x数组
def getXArray(start_x, end_x, n):
    array_x = [0.0 for _ in range(n + 1)]
    h = (end_x - start_x) / n
    for i in range(n + 1):
        array_x[i] = start_x + i * h
    return array_x


# 用户交互模式，输入函数f, 区间范围[start_x, end_x]，等分次数n，插值点point_x
def getInput1():
    fun_str = input("Please enter the function(use x only): ")
    fun = sympify(fun_str)
    n = int(input("Please enter n: "))
    start_x = eval(input("Please enter x0: "))
    end_x = eval(input("Please enter xn: "))
    array_x = getXArray(start_x, end_x, n)
    point_x = eval(input("Please input interpolation point: "))
    return fun, n, array_x, point_x


# 直接设置数据，便于展示结果
def setInput1(fun_str, n, start_x, end_x, point_x):
    fun = sympify(fun_str)
    array_x = getXArray(start_x, end_x, n)
    return fun, n, array_x, point_x


# 用户交互模式，输入函数f, 区间范围[start_x, end_x],n,array_x数组，插值点point_x
def getInput2():
    fun_str = input("Please enter the function(use x only): ")
    fun = sympify(fun_str)
    n = int(input("Please enter n: "))
    array_x = [0.0 for _ in range(n + 1)]
    print("Please enter x:")
    input_x = input().split(' ')
    for i in range(n + 1):
        array_x[i] = eval(input_x[i])
    point_x = eval(input("Please input interpolation point: "))
    return fun, n, array_x, point_x


# 直接设置数据
def setInput2(fun_str, n, array_x, point_x):
    fun = sympify(fun_str)
    return fun, n, array_x, point_x


def getAns(fun, n, array_x, point_x):
    y = 0.0
    k = 0
    while k <= n:
        l = 1.0
        for j in range(n + 1):
            if j == k:
                continue
            l *= (point_x - array_x[j]) / (array_x[k] - array_x[j])
        y += l * fun.subs(x, array_x[k])
        k += 1

    print("\t\t\tx = {}, y = {}, accurate y = {}".format(point_x, y, fun.subs(x, point_x).evalf()))


print("问题1：")
print("\t(1): ")
print("\t\tn = 5: ")
getAns(*setInput1("1/(1+x^2)", 5, -5, 5, 0.75))
getAns(*setInput1("1/(1+x^2)", 5, -5, 5, 1.75))
getAns(*setInput1("1/(1+x^2)", 5, -5, 5, 2.75))
getAns(*setInput1("1/(1+x^2)", 5, -5, 5, 3.75))
getAns(*setInput1("1/(1+x^2)", 5, -5, 5, 4.75))
print("\t\tn = 10: ")
getAns(*setInput1("1/(1+x^2)", 10, -5, 5, 0.75))
getAns(*setInput1("1/(1+x^2)", 10, -5, 5, 1.75))
getAns(*setInput1("1/(1+x^2)", 10, -5, 5, 2.75))
getAns(*setInput1("1/(1+x^2)", 10, -5, 5, 3.75))
getAns(*setInput1("1/(1+x^2)", 10, -5, 5, 4.75))
print("\t\tn = 20: ")
getAns(*setInput1("1/(1+x^2)", 20, -5, 5, 0.75))
getAns(*setInput1("1/(1+x^2)", 20, -5, 5, 1.75))
getAns(*setInput1("1/(1+x^2)", 20, -5, 5, 2.75))
getAns(*setInput1("1/(1+x^2)", 20, -5, 5, 3.75))
getAns(*setInput1("1/(1+x^2)", 20, -5, 5, 4.75))
print("\t(2): ")
print("\t\tn = 5: ")
getAns(*setInput1("exp(x)", 5, -1, 1, -0.95))
getAns(*setInput1("exp(x)", 5, -1, 1, -0.05))
getAns(*setInput1("exp(x)", 5, -1, 1, 0.05))
getAns(*setInput1("exp(x)", 5, -1, 1, 0.95))
print("\t\tn = 10: ")
getAns(*setInput1("exp(x)", 10, -1, 1, -0.95))
getAns(*setInput1("exp(x)", 10, -1, 1, -0.05))
getAns(*setInput1("exp(x)", 10, -1, 1, 0.05))
getAns(*setInput1("exp(x)", 10, -1, 1, 0.95))
print("\t\tn = 20: ")
getAns(*setInput1("exp(x)", 20, -1, 1, -0.95))
getAns(*setInput1("exp(x)", 20, -1, 1, -0.05))
getAns(*setInput1("exp(x)", 20, -1, 1, 0.05))
getAns(*setInput1("exp(x)", 20, -1, 1, 0.95))

print("问题2：")
print("\t(1): ")
print("\t\tn = 5: ")
getAns(*setInput1("1/(1+x^2)", 5, -1, 1, -0.95))
getAns(*setInput1("1/(1+x^2)", 5, -1, 1, -0.05))
getAns(*setInput1("1/(1+x^2)", 5, -1, 1, 0.05))
getAns(*setInput1("1/(1+x^2)", 5, -1, 1, 0.95))
print("\t\tn = 10: ")
getAns(*setInput1("1/(1+x^2)", 10, -1, 1, -0.95))
getAns(*setInput1("1/(1+x^2)", 10, -1, 1, -0.05))
getAns(*setInput1("1/(1+x^2)", 10, -1, 1, 0.05))
getAns(*setInput1("1/(1+x^2)", 10, -1, 1, 0.95))
print("\t\tn = 20: ")
getAns(*setInput1("1/(1+x^2)", 20, -1, 1, -0.95))
getAns(*setInput1("1/(1+x^2)", 20, -1, 1, -0.05))
getAns(*setInput1("1/(1+x^2)", 20, -1, 1, 0.05))
getAns(*setInput1("1/(1+x^2)", 20, -1, 1, 0.95))
print("\t(2): ")
print("\t\tn = 5: ")
getAns(*setInput1("exp(x)", 5, -5, 5, -4.75))
getAns(*setInput1("exp(x)", 5, -5, 5, -0.25))
getAns(*setInput1("exp(x)", 5, -5, 5, 0.05))
getAns(*setInput1("exp(x)", 5, -5, 5, 4.75))
print("\t\tn = 10: ")
getAns(*setInput1("exp(x)", 10, -5, 5, -4.75))
getAns(*setInput1("exp(x)", 10, -5, 5, -0.25))
getAns(*setInput1("exp(x)", 10, -5, 5, 0.05))
getAns(*setInput1("exp(x)", 10, -5, 5, 4.75))
print("\t\tn = 20: ")
getAns(*setInput1("exp(x)", 20, -5, 5, -4.75))
getAns(*setInput1("exp(x)", 20, -5, 5, -0.25))
getAns(*setInput1("exp(x)", 20, -5, 5, 0.05))
getAns(*setInput1("exp(x)", 20, -5, 5, 4.75))

print("问题4：")
print("\t(1): ")
print("\t\t插值节点：", [1, 4, 9])
getAns(*setInput2("sqrt(x)", 2, [1, 4, 9], 5))
getAns(*setInput2("sqrt(x)", 2, [1, 4, 9], 50))
getAns(*setInput2("sqrt(x)", 2, [1, 4, 9], 115))
getAns(*setInput2("sqrt(x)", 2, [1, 4, 9], 185))
print("\t(2): ")
print("\t\t插值节点：", [36, 49, 64])
getAns(*setInput2("sqrt(x)", 2, [36, 49, 64], 5))
getAns(*setInput2("sqrt(x)", 2, [36, 49, 64], 50))
getAns(*setInput2("sqrt(x)", 2, [36, 49, 64], 115))
getAns(*setInput2("sqrt(x)", 2, [36, 49, 64], 185))
print("\t(3): ")
print("\t\t插值节点：", [100, 121, 144])
getAns(*setInput2("sqrt(x)", 2, [100, 121, 144], 5))
getAns(*setInput2("sqrt(x)", 2, [100, 121, 144], 50))
getAns(*setInput2("sqrt(x)", 2, [100, 121, 144], 115))
getAns(*setInput2("sqrt(x)", 2, [100, 121, 144], 185))
print("\t(4): ")
print("\t\t插值节点：", [169, 196, 225])
getAns(*setInput2("sqrt(x)", 2, [169, 196, 225], 5))
getAns(*setInput2("sqrt(x)", 2, [169, 196, 225], 50))
getAns(*setInput2("sqrt(x)", 2, [169, 196, 225], 115))
getAns(*setInput2("sqrt(x)", 2, [169, 196, 225], 185))

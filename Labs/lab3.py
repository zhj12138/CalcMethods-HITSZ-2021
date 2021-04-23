import sympy
from sympy import *
x = Symbol('x')
y = Symbol('y')


# 用户交互
def getInput():
    fun_str = input("Please enter the function(use x and y only): ")
    fun = sympify(fun_str)
    a = eval(input("Please enter a: "))
    b = eval(input("Please enter b: "))
    alpha = eval(input("Please enter alpha: "))
    N = int(input("Please enter N: "))
    accu_fun_str = input("Please enter the accurate function: ")
    accu_fun = simplify(accu_fun_str)
    return fun, a, b, alpha, N, accu_fun


# 直接设置
def setInput(fun_str, a, b, alpha, N, accu_fun_str):
    fun = sympify(fun_str)
    accu_fun = sympify(accu_fun_str)
    return fun, a, b, alpha, N, accu_fun


def getAns(fun, a, b, alpha, N, accu_fun):
    print("\t\tN={}: ".format(N))
    x0 = a
    y0 = alpha
    h = (b - a) / N
    for n in range(1, N + 1):
        K1 = h * fun.subs([(x, x0), (y, y0)])
        K2 = h * fun.subs([(x, x0 + h / 2), (y, y0 + K1 / 2)])
        K3 = h * fun.subs([(x, x0 + h / 2), (y, y0 + K2 / 2)])
        K4 = h * fun.subs([(x, x0 + h), (y, y0 + K3)])
        x1 = x0 + h
        y1 = y0 + 1 / 6 * (K1 + 2 * K2 + 2 * K3 + K4)
        print("\t\t\tx{} = {}, y{} = {}, accurate y{} = {}".format(n, x1, n, y1.evalf(), n, accu_fun.subs(x, x1).evalf()))
        x0 = x1
        y0 = y1


print("问题1：")
print("\t(1): ")
getAns(*setInput("x+y", 0, 1, -1, 5, "-x-1"))
getAns(*setInput("x+y", 0, 1, -1, 10, "-x-1"))
getAns(*setInput("x+y", 0, 1, -1, 20, "-x-1"))
print("\t(2): ")
getAns(*setInput("-y^2", 0, 1, 1, 5, "1/(x+1)"))
getAns(*setInput("-y^2", 0, 1, 1, 10, "1/(x+1)"))
getAns(*setInput("-y^2", 0, 1, 1, 20, "1/(x+1)"))
print("问题2：")
print("\t(1): ")
getAns(*setInput("2/x*y+x^2*exp(x)", 1, 3, 0, 5, "x^2*(exp(x)-exp(1))"))
getAns(*setInput("2/x*y+x^2*exp(x)", 1, 3, 0, 10, "x^2*(exp(x)-exp(1))"))
getAns(*setInput("2/x*y+x^2*exp(x)", 1, 3, 0, 20, "x^2*(exp(x)-exp(1))"))
print("\t(2): ")
getAns(*setInput("1/x*(y^2+y)", 1, 3, -2, 5, "2*x/(1-2*x)"))
getAns(*setInput("1/x*(y^2+y)", 1, 3, -2, 10, "2*x/(1-2*x)"))
getAns(*setInput("1/x*(y^2+y)", 1, 3, -2, 20, "2*x/(1-2*x)"))
print("问题3：")
print("\t(1): ")
getAns(*setInput("-20*(y-x^2)+2*x", 0, 1, 1/3, 5, "x^2+1/3*exp(-20*x)"))
getAns(*setInput("-20*(y-x^2)+2*x", 0, 1, 1/3, 10, "x^2+1/3*exp(-20*x)"))
getAns(*setInput("-20*(y-x^2)+2*x", 0, 1, 1/3, 20, "x^2+1/3*exp(-20*x)"))
print("\t(2): ")
getAns(*setInput("-20*y+20*sin(x)+cos(x)", 0, 1, 1, 5, "exp(-20*x)+sin(x)"))
getAns(*setInput("-20*y+20*sin(x)+cos(x)", 0, 1, 1, 10, "exp(-20*x)+sin(x)"))
getAns(*setInput("-20*y+20*sin(x)+cos(x)", 0, 1, 1, 20, "exp(-20*x)+sin(x)"))
print("\t(3): ")
getAns(*setInput("-20*(y-exp(x)*sin(x))+exp(x)*(sin(x)+cos(x))", 0, 1, 0, 5, "exp(x)*sin(x)"))
getAns(*setInput("-20*(y-exp(x)*sin(x))+exp(x)*(sin(x)+cos(x))", 0, 1, 0, 10, "exp(x)*sin(x)"))
getAns(*setInput("-20*(y-exp(x)*sin(x))+exp(x)*(sin(x)+cos(x))", 0, 1, 0, 20, "exp(x)*sin(x)"))

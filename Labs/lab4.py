from sympy import *
x = Symbol('x')


def getInput():
    fun_str = input("Please enter the function(use x only): ")
    fun = sympify(fun_str)
    dfun = diff(fun)
    e1 = eval(input("Please enter e1: "))
    e2 = eval(input("Please enter e2: "))
    N = int(input("Please enter N: "))
    x0 = eval(input("Please enter x0: "))
    return fun, dfun, e1, e2, N, x0


def setInput(fun_str, e1, e2, N, x0):
    fun = sympify(fun_str)
    dfun = diff(fun)
    return fun, dfun, e1, e2, N, x0


def getAns(fun, dfun, e1, e2, N, x0):
    n = 1
    while n <= N:
        F = fun.subs(x, x0)
        DF = dfun.subs(x, x0)
        if abs(F) < e1:
            print("\t\t", x0.evalf())
            return
        if abs(DF) < e2:
            print("\t\tFail")
            return
        x1 = x0 - F / DF
        Tol = abs(x1 - x0)
        if abs(Tol) < e1:
            print("\t\t", x1.evalf())
            return
        n += 1
        x0 = x1
    print("\t\tFail")


print("问题1：")
print("\t(1): ")
getAns(*(setInput("cos(x)-x", 1e-6, 1e-4, 10, pi/4)))
print("\t(2): ")
getAns(*(setInput("exp(-x)-sin(x)", 1e-6, 1e-4, 10, 0.6)))

print("问题2：")
print("\t(1): ")
getAns(*(setInput("x-exp(-x)", 1e-6, 1e-4, 10, 0.5)))
print("\t(2): ")
getAns(*(setInput("x^2-2*x*exp(-x)+exp(-2*x)", 1e-6, 1e-4, 20, 0.5)))

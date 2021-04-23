def getInput():
    n = int(input("Please enter n: "))
    print("Please enter the matrix: ")
    a = [[0.0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        strin = input().split(' ')
        for j in range(1, n + 1):
            a[i][j] = eval(strin[j - 1])
    b = [0.0 for _ in range(n + 1)]
    print("Please enter b: ")
    strin = input().split(' ')
    for i in range(1, n + 1):
        b[i] = eval(strin[i - 1])
    return n, a, b


def setInput(n, a, b):
    # 将下标都往后移动一位
    a.insert(0, [0.0 for _ in range(n + 1)])
    for i in range(1, n + 1):
        a[i].insert(0, 0.0)
    b.insert(0, 0.0)
    return n, a, b


def getAns(n, a, b):
    for k in range(1, n):
        p = k
        for j in range(k, n + 1):
            if abs(a[j][k]) > abs(a[p][k]):
                p = j
        if a[p][k] == 0:
            print("奇异")
            exit(0)
        if p != k:
            for i in range(1, n + 1):
                tmp = a[k][i]
                a[k][i] = a[p][i]
                a[p][i] = tmp
            tmp = b[p]
            b[p] = b[k]
            b[k] = tmp
        for i in range(k + 1, n + 1):
            m = a[i][k] / a[k][k]
            for j in range(k, n + 1):
                a[i][j] -= a[k][j] * m
            b[i] -= b[k] * m

    if a[n][n] == 0:
        print("奇异")
        exit(0)

    x = [0.0 for _ in range(n + 1)]
    for k in range(n, 0, -1):
        tmp = 0
        for j in range(k + 1, n + 1):
            tmp += a[k][j] * x[j]
        x[k] = (b[k] - tmp) / a[k][k]

    for i in range(1, n + 1):
        print("\t\t\tx{} = {}".format(i, x[i]))


print("问题1：")
print("\t(1): ")
getAns(*setInput(4, [[0.4096, 0.1234, 0.3678, 0.2943],
                     [0.2246, 0.3872, 0.4015, 0.1129],
                     [0.3645, 0.1920, 0.3781, 0.0643],
                     [0.1784, 0.4002, 0.2786, 0.3927]],
                 [1.1951, 1.1262, 0.9989, 1.2499]))
print("\t(2): ")
getAns(*setInput(4, [[136.01, 90.860, 0, 0],
                     [90.860, 98.810, -67.590, 0],
                     [0, -67.590, 132.01, 46.260],
                     [0, 0, 46.260, 177.17]],
                 [226.87, 122.08, 110.68, 223.43]))
print("\t(3): ")
getAns(*setInput(4, [[1, 1/2, 1/3, 1/4],
                     [1/2, 1/3, 1/4, 1/5],
                     [1/3, 1/4, 1/5, 1/6],
                     [1/4, 1/5, 1/6, 1/7]],
                 [25/12, 77/60, 57/60, 319/420]))
print("\t(4): ")
getAns(*setInput(4, [[10, 7, 8, 7],
                     [7, 5, 6, 5],
                     [8, 6, 10, 9],
                     [7, 5, 9, 10]],
                 [32, 23, 33, 31]))
print("问题2：")
print("\t(1): ")
getAns(*setInput(4, [[197, 305, -206, 804],
                     [46.8, 71.3, -47.4, 52.0],
                     [88.6, 76.4, -10.8, 802],
                     [1.45, 5.90, 6.13, 36.5]],
                 [136, 11.7, 25.1, 6.60]))
print("\t(2): ")
getAns(*setInput(4, [[0.5398, 0.7161, -0.5554, -0.2982],
                     [0.5257, 0.6924, 0.3565, -0.6255],
                     [0.6465, -0.8187, -0.1872, 0.1291],
                     [0.5814, 0.9400, -0.7779, -0.4042]],
                 [0.2058, -0.0503, 0.1070, 0.1859]))
print("\t(3): ")
getAns(*setInput(3, [[10, 1, 2],
                     [1, 10, 2],
                     [1, 1, 5]],
                 [13, 13, 7]))
print("\t(4): ")
getAns(*setInput(3, [[4, -2, -4],
                     [-2, 17, 10],
                     [-4, 10, 9]],
                 [-2, 25, 15]))



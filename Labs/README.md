## 环境依赖

我的`python`版本为`python3.9`(低一点的`python3`版本应该也没问题)。

具体依赖可查看`requirements.txt`(其实只使用了`sympy`一个第三方库:joy:)，可直接使用以下指令安装依赖：

```shell
pip install -r requirements.txt
```

## 目录结构

`lab1.py`是实验题目1的源文件，`lab1_result.txt`是实验题目1的输出结果。

依此类推...

## 查看输出结果

### 一次性查看所有实验题的结果

```shell
python all.py
```

或者重定向到`all.txt`(如果中文乱码了，请自行更改文件编码:joy:)：

```shell
python all.py > all.txt
```

### 单独查看实验题的结果

```shell
python lab1.py
```

亦或者重定向到txt文件：

```shell
python lab1.py > lab1_result.txt
```

依此类推...



当然，你也可以直接查看我已经运行出来的结果。
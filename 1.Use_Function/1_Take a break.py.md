# 1_Take a break.py

### 目标：

> 完成第一个 Python 程序：每隔一段时间，打开同一个视频播放页面，提示自己需要休息



#### 假设目前为止我并没有任何编码的经验（实际也基本没有...），不知道什么是方法、什么是类、怎样做循环，我依然可以依照一套固定的方法去完成这个项目

注：由于是第一次上手的程序，以下暂不纠结于方法、功能、函数等概念



## Step 1：明确一个大的目标

每隔一段时间打开同一个视频播放页面，提示自己需要休息



## Step 2：将大目标拆解为小目标

为了实现大目标，需要按照什么步骤去做？

##### 可以将这些步骤作为注释写在编辑器里：

```
# 1. 程序等待一段时间
# 2. 打开一个指定的页面
# 3. 重复1-2
```



## Step 3：善用搜索实现小目标

举例：如何打开一个指定的页面？

```
# 2. 打开一个指定的页面
```

##### 使用 Chrome 搜索：“Python open a webpage ” 或者任何相关的关键字，发现一个用于打开网页的方法 webbrowser：

```python
webbrowser.open('')
```

我们可以得到以下代码：

```python
webbrowser.open('https://docs.python.org/3.5/contents.html')
```



## Step 4：试运行并解决报错

得到运行报错：

```python
Traceback (most recent call last):
  File "/Users/breaking_red/Python/U_take_a_break.py", line 13, in <module>
    webbrowser.open('https://docs.python.org/2/library/webbrowser.html')
NameError: name 'webbrowser' is not defined
```

报错指出了问题出现在第13行，并给出了错误的语句和原因：webbrowser 没有定义

##### 通过 Google 可以发现 webbrowser 是 Python 标准库里提供的一个功能？需要进行 import



## Step 5：重复 3-4 完成所有小目标

更正报错信息中指出的 Bug：

```python
# 2. 打开一个指定页面
import webbrowser
webbrowser.open('https://docs.python.org/3.5/contents.html')
```

重复 3-4 完成其他小目标：

1. 程序等待

```
# 1. 程序等待一段时间
```

使用 Chrome 搜索：“Python wait for a time ” 或者任何相关的关键字，发现功能 time，我们以 3s为等待间隔来进行程序测试：

```python
time.sleep(3)
```

引用这个功能：

```python
import time
import webbrowser
# 1. 程序等待一段时间
time.sleep(3)
# 2.打开一个指定页面
webbrowser.open('https://docs.python.org/3.5/contents.html')
```



2. 加入循环

#####    Google 如何在 Python 中加入循环？可以得到一些要领，试图在代码中加入 3次循环：

- 设置变量
- 使用 while
- 用缩进控制哪些代码块在 while 中

```python
import time
import webbrowser
# 3. 设置循环
loop_time = 0
ammount_time = 3
while loop_time < ammount_time:
# 1. 程序等待一段时间
  time.sleep(3)
# 2.打开一个指定页面
  webbrowser.open('https://docs.python.org/3.5/contents.html')
  loop_time = loop_time + 1
```



## Step 6：尝试进行优化

思考程序如何做的更好？

- 打开网页-关闭网页-刷新网页
- 显示程序运行开始的时间
- ...
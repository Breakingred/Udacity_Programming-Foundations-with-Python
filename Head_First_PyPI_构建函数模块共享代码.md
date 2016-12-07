# ?Head_First_在PyPI共享函数模块（module）

### - 目标

>  创建、安装、发布可共享模块，加载到PyPI，掌握函数相关新技能



###- 步骤 

#### 1. 将函数(function)转换为——模块(module)

> 函数：一个命名的代码组
>
> 模块：一个 .py 文件

1、添加注释

2、本地执行、测试模块以重置 Python 解释器

```python
""" nester.py 模块提供了一个函数 print_list() ，这个函数可以用于打印包含嵌套列表的列表 """
def print_list(thelist):
    for each_item in thelist: 
        if isinstance(each_item,list):
            print_list(each_item)
        else:
            print(each_item)
```

```python
=============== RESTART: /Users/breaking_red/Python/nester.py ===============
>>> movies=['a',11,['a1',['a2','a3']]]
>>> print_list(movies)
a
11
a1
a2
a3
>>> 
```

#### 2. 准备发布

> 发布：distribution， 一个文件集合，这些文件联合在一起允许你构建、打包发布你的模块

1、为模块创建一个文件夹 nester，将 .py 模块文件复制到这个文件夹

2 、在文件夹中新建一个名为 setup.py 的文件，这个文件包含有关发布的元数据：

​	***？py_modules***

​	***？setup 参数末尾有 ,***

```python
# 从 Python 发布工具导入“setup”函数
from distutils.core import setup
# setup 函数提供了一些参数，需要将模块的元数据与 setup 函数的参数关联
setup(
    name = 'nester',
    version = '1.0.0',
    py_modules = ['nester'],
    author = 'echo',
    author_email = 'hhwei.procrastination@gmail.com',
    url = 'https://github.com/Breakingred',
    description = 'A simple printer of nested lists',)
```

#### 3. 构建发布

1、打开终端，在 nester 文件夹路径下键入命令，终端返回的消息确认发布已创建

```
python3 setup.py sdist
```

​	***？warning 提示缺失了 readme 及其他可选的附加文件***

```
localhost:nester breaking_red$ python3 setup.py sdist
running sdist
running check
warning: sdist: manifest template 'MANIFEST.in' does not exist (using default file list)

warning: sdist: standard file not found: should have one of README, README.txt

writing manifest file 'MANIFEST'
creating nester-1.0.0
making hard links in nester-1.0.0...
hard linking nester.py -> nester-1.0.0
hard linking setup.py -> nester-1.0.0
creating dist
Creating tar archive
removing 'nester-1.0.0' (and everything under it)
localhost:nester breaking_red$

```

2、在终端键入命令，将发布安装到 Python 的本地副本中

```
sudo python3 setup.py install
```

```
localhost:nester breaking_red$ sudo python3 setup.py install
Password:
Sorry, try again.
Password:
running install
running build
running build_py
creating build
creating build/lib
copying nester.py -> build/lib
running install_lib
copying build/lib/nester.py -> /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages
byte-compiling /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/nester.py to nester.cpython-35.pyc
running install_egg_info
Writing /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/nester-1.0.0-py3.5.egg-info
localhost:nester breaking_red$
```

#### 4. 发布预览

​	***？与书中相比，缺失了 nester.pyc 文件（编译版本的代码）***

查看 nester 文件夹，发现发布工具向文件夹中添加了 MANIFEST、build、dist 等文件

#### 5. 导入模块并使用

要使用一个模块，只需要把它导入到你的程序中，回想 Take_a_Break 项目中的 import webbrowser，正是导入了一个有打开网页功能的模块

```python
# 关键字 import + 模块名
import nester
```

现在就将模块 nester 包含在程序中了，可以直接使用模块 nester 中的函数了（可能不止一个）？测试：

```
import nester
cast = ['Palin','Cleese','Idle','Jones','Gilliam','Chapman']
print_list(cast)
```

结果不行啊，显示 print_list() 这个函数没有定义

```
============= RESTART: /Users/breaking_red/Python/test_import.py =============
Traceback (most recent call last):
  File "/Users/breaking_red/Python/test_import.py", line 3, in <module>
    print_list(cast)
NameError: name 'print_list' is not defined
>>> 
```

这跟之前 import 了 webbrowser，然后就直接用了 webbrowser.open() 的区别是？需要在函数前加上模块名称！

```
# 模块名.函数名(要处理的对象)
nester.print_list(cast)
```

终于OK了

> Python 的模块实现命名空间，命名空间名就像是姓氏

```
============= RESTART: /Users/breaking_red/Python/test_import.py =============
Palin
Cleese
Idle
Jones
Gilliam
Chapman
>>> 
```

#### 6. 将模块上传至 PyPI

1、通过命令行窗口注册 PyPI （首次上传需要）

2、通过命令行窗口上传

```
localhost:nester breaking_red$ python3 setup.py register
running register
running check
We need to know who you are, so please choose either:
 1. use your existing login,
 2. register as a new user,
 3. have the server generate a new password for you (and email it to you), or
 4. quit
Your selection [default 1]:
1
Username: BreakingRed
Password:
Registering nester to https://pypi.python.org/pypi
Server response (403): You are not allowed to store 'nester' package information
localhost:nester breaking_red$
```

***？提示我 nester 这个模块名称被占用，都有哪里的名称需要修改？还是说需要重头搞起？***


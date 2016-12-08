

# Head_First_列表-创建函数



### - 目标：

> 将影城电影列表进行打印输出，电影列表是一个嵌套列表，其中包括演员列表、配乐列表、工作人员列表等

### - 构建列表：

1. 只存储电影名称

```python
# 只存储电影名称
movies = ['The Holy Grail','---','The Life of Brain','---','The meaning of Life']
```

2. 加入电影上映年份等元素

```python
# 加上电影上映年份，可以试着使用列表方法修改原列表
movies = ['The Holy Grail','---','The Life of Brain','---','The meaning of Life']
# 使用 insert()插入在指定位置前
movies.insert(2,1975)
# 列表元素增加了，注意OFFSET即数值偏移量
movies.insert(5,1979)
# 使用 append()在列表末尾追加元素
movies.append(1983)
```

```python
# 也可以选择重新创建列表
movies = ['The Holy Grail',1975,'---','The Life of Brain',1979,'---','The meaning of Life',1983]
```



### - 处理列表

1. 将列表数据显示出来

```python
# 使用 for 迭代处理列表
movies = ['The Holy Grail',1975,'---','The Life of Brain',1979,'---','The meaning of Life',1983]
for each_item in movies:
    print(each_item)
```
```python
# 使用 for 比使用 while 要好，while 需要计数
count = 0
while count < len(movies):
    print(movies[count])
    count = count+1    
```



### - 嵌套的列表

1. 创建嵌套列表

```python
# 每个电影中的演员也是一个列表，演员列表包含配角列表
movies = ['The Holy Grail',1975,['Graham',['Chapmam','Eric','John']],'---','The Life of Brain',1979,['Idle',['Terry','Michael']],'---','The meaning of Life',1983,['Echo',['Christina','Jones']]]
# 试着输出
for each_item in movies:
    print(each_item)
```

可以发现嵌套列表作为一级列表的元素被作为列表输出了

```python
The Holy Grail
1975
['Graham', ['Chapmam', 'Eric', 'John']]
---
The Life of Brain
1979
['Idle', ['Terry', 'Michael']]
---
The meaning of Life
1983
['Echo', ['Christina', 'Jones']]
```

2. 优化输出

```python
movies = ['The Holy Grail',1975,['Graham',['Chapmam','Eric','John']],'---','The Life of Brain',1979,['Idle',['Terry','Michael']],'---','The meaning of Life',1983,['Echo',['Christina','Jones']]]
# 使用 if 判断正在输出的列表元素是否为列表，如果是，则输出列表内的元素，如果不是，则输出当前元素
for each_item in movies:
    # 使用 BIF isinstance() 判断列表元素的类型  
    if isinstance(each_item,list):
        # 要考虑到这是两层列表的嵌套
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)
```
```python
========== RESTART: /Users/breaking_red/Python/print_movies_list.py ==========
The Holy Grail
1975
Graham
Chapmam
Eric
John
---
The Life of Brain
1979
Idle
Terry
Michael
---
The meaning of Life
1983
Echo
Christina
Jones
>>> 
```

### - 创建函数！避免重复代码

1. 找出重复的代码
2. def + 函数名称 + 参数 + : + 函数代码组
3. 函数要在代码组中调用自身

```python
movies = ['The Holy Grail',1975,['Graham',['Chapmam','Eric','John']],'---','The Life of Brain',1979,['Idle',['Terry','Michael']],'---','The meaning of Life',1983,['Echo',['Christina','Jones']]]

def print_list(thelist):
    for each_item in thelist: 
        if isinstance(each_item,list):
            print_list(each_item)
        else:
            print(each_item)
   
print_list(movies)
```

### - Reflection


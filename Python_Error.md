# Python_Error

### 1. inconsistent use of tabs and spaces in indentation

在缩进时 Tab 和 Space 的使用反常/不一致，多出现在需要缩进的代码块如判断、循环等处，与编辑器有关

##### Pep8：优先使用 Space 来缩进，不能混用 Tab 和 Space！

>  Python has Pep8, a document which lists "good python style" which explicitly states that 4 spaces is the accepted form on indentation. 

[Spaces are the preferred indentation method.Use 4 spaces per indentation level.Python 3 disallows mixing the use of tabs and spaces for indentation.](https://www.python.org/dev/peps/pep-0008/)

> Don't use tabs.
>
> 1. Set your editor to use 4 **spaces** for indentation.
> 2. Make a search and replace to replace all tabs with 4 spaces.
> 3. Make sure your editor is set to **display** tabs as 8 spaces.
>
> Note: The reason for 8 spaces for tabs is so that you immediately notice when tabs have been inserted unintentionally - such as when copying and pasting from example code that uses tabs instead of spaces.



### 2. ？IDLE 编辑窗口无法输入中文

待解决，参考链接：

https://github.com/OpenMindClub/OMOOC2py/issues/54

https://www.zhihu.com/question/26532408



### 3. ？使用 os.listdir() 查看目录下文件时显示的 '.DS_Store' 是什么文件

MacOSX中一种存储文件夹元数据的系统文件

> .DS_Store files are used by Mac OS X to store folder specific metadata information. They are created in every folder that Mac OS X Finder accesses, even network volumes and external devices.

[？是否可以删除/停止生成这个文件](http://osxdaily.com/2009/12/31/what-is-a-ds_store-file/)

[如何停止文件生成](http://stackoverflow.com/questions/18015978/how-to-stop-creating-ds-store-on-mac)



### 4. Difference between Method & Function

方法、函数的区别：

1）built-in type 里 string 对应的可以直接使用的 str.strip() 

2）标准库里 os 模块的函数 os.rename()，需要 import

3）自己定义的函数 def print_list()，需要 import



> In general: methods are functions that belong to a class, functions can be on any other scope of the code so you could state that all methods are functions, but not all functions are methods:
>
> Take the following python example:
>
> ```
> class Door:
>   def open(self):
>     print 'hello stranger'
>
> def knock_door:
>   a_door = Door()
>   Door.open(a_door)
>
> knock_door()
>
> ```
>
> The example given shows you a class called "Door" which has a method or action called "open", it is called a method because it was declared inside a class. There is another portion of code with "def" just below which defines a function, it is a function because it is not declared inside a class, this function calls the method we defined inside our class as you can see and finally the function is being called by itself.
>
> As you can see you can call a function anywhere but if you want to call a method either you have to pass a new object of the same type as the class the method is declared (Class.method(object)) or you have to invoke the method inside the object (object.Method()), at least in python.
>
> Think of methods as things only one entity can do, so if you have a Dog class it would make sense to have a bark function only inside that class and that would be a method, if you have also a Person class it could make sense to write a function "feed" for that doesn't belong to any class since both humans and dogs can be fed and you could call that a function since it does not belong to any class in particular.






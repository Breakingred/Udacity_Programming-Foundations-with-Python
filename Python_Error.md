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


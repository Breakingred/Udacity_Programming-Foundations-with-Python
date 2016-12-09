# 1_Planning_secret_massage.py

### Step1：大目标

对文件夹中的文件进行重命名，去掉文件名中的数字

### Step2：步骤

```python
# 获取文件夹中的文件名称，组成一个待处理的字符串列表
# 获取一个字符串，去掉其中的数字
# 获取下一个字符串，循环处理
```

### Step3：解决问题

1. 获取文件名称

```python
import os
#def rename_files():   
# 获取文件夹中的文件名称，组成一个待处理的字符串列表
list_name = os.listdir("/Users/breaking_red/Udacity_Programming-Foundations-with-Python/1.Use_Function/Planning_secret_massage_pic")
print(list_name)
# 循环处理列表,获取一个字符串，去掉其中的数字
for each_name in list_name    
#rename_files()
```

.DS_Store 文件为 MacOSX生成的存储文件夹元数据的系统文件，可暂且忽略

```
>>> 
 RESTART: /Users/breaking_red/Udacity_Programming-Foundations-with-Python/1.Use_Function/U_rename_file_names.py 
['.DS_Store', '16los angeles.jpg', '17cairo.jpg', '22rochester.jpg', '25madrid.jpg', '28houston.jpg', '29bristol.jpg', '29buenos aires.jpg', '2chennai.jpg', '2hyderabad.jpg', '35miami.jpg', '36sydney.jpg', '37athens.jpg', '41seoul.jpg', '45austin.jpg', '45ithaca.jpg', '46colombo.jpg', '47london.jpg', '47sao paulo.jpg', '47singapore.jpg', '48sunnyvale.jpg', '4istanbul.jpg', '50san diego.jpg', '52new york.jpg', '54dallas.jpg', '55kiev.jpg', '5bogota.jpg', '61edinbrugh.jpg', '64seattle.jpg', '66san jose.jpg', '68pune.jpg', '69chicago.jpg', '69shanghai.jpg', '72bangalore.jpg', '72bucharest.jpg', '73delhi.jpg', '74tel aviv.jpg', '83gainesville.jpg', '88jacksonville.jpg', '89berkeley.jpg', '90beijing.jpg', '93manchester.jpg', '96karachi.jpg', '97oakland.jpg', '9barcelona.jpg']
>>> 
```

2. 处理文件名，去掉其中的数字

```python
import os
def rename_files():    
    list_name = os.listdir("/Users/breaking_red/Udacity_Programming-Foundations-with-Python/1.Use_Function/Planning_secret_massage_pic")
# 获取文件夹中的文件名称，组成一个待处理的字符串列表
    saved_path = os.getcwd()
    print('current path'+ saved_path)
    os.chdir('/Users/breaking_red/Udacity_Programming-Foundations-with-Python/1.Use_Function/Planning_secret_massage_pic')
# 循环处理列表,获取一个字符串，去掉其中的数字
    for old_name in list_name:
        os.rename(old_name,old_name.strip('0123456789'))
    os.chdir(saved_path)

rename_files()
```
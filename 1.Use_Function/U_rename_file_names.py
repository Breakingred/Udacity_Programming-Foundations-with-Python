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

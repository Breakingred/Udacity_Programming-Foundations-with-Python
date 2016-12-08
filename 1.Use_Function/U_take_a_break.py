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

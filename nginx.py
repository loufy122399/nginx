#!/usr/bin/env python
#coding:utf-8
status_200= []
status_404= []
with open("access_json.log") as f:
for line in f.readlines():
line = eval(line)                             #字符串转换成字典
if line.get("status") == "200":               #字典 get() 函数返回指定键的值
status_200.append(line.get)
elif line.get("status") == "404":
status_404.append(line.get)
else:
print("状态码 ERROR")
f.close()
print "状态码200的有--:",len(status_200)
print "状态码404的有--:",len(status_404)

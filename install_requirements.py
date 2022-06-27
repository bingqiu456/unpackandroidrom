#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
执行此文件将自动安装requirements.txt中的依赖
'''
import os,platform
f=open('requirements.txt',"r+",encoding="utf_8")
for i in f:
    if i.strip("\ufeff")[0]=='#':
        pass
    else:
        os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple '+i)
f.close()
if platform.system()=='Linux':print('请手动安装brotli')

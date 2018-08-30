import zipfile
import os
import time

import threading

#定义函数

def fun_timer():
     zip_ya()
     global timer  #定义变量
     timer = threading.Timer(60 * 60,fun_timer)   #60秒调用一次函数
     timer.start()    #启用定时器


def zip_ya():
       print('开始备份...........')  # 打印输出
       startdir = "../582010"  #要压缩的文件夹路径
       file_news = str(time.time()) + 'back.zip' # 压缩后文件夹的名字
       z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) #参数一：文件夹名
       ifSuccess = False
       for dirpath, dirnames, filenames in os.walk(startdir):
           print('目录：' + str(dirpath))
           fpath = dirpath.replace(startdir,'') #这一句很重要，不replace的话，就从根目录开始复制
           fpath = fpath and fpath + os.sep or ''#这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
           for filename in filenames:
               z.write(os.path.join(dirpath, filename),fpath+filename)
               print ('压缩成功')
               ifSuccess = True
       z.close()
       if ifSuccess:
            print('备份完成' + file_news + '...........')# 打印输出
       else:
            print('备份失败' + file_news + '...........')# 打印输出

if __name__=="__main__":
    timer = threading.Timer(1, fun_timer)  # 首次启动
    timer.start()
    #startdir = "D:\Game\Steam\\userdata\275688468\582010"  #要压缩的文件夹路径
    #file_news = startdir +'.zip' # 压缩后文件夹的名字
    #zip_ya(startdir,file_news)
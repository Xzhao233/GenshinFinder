import os
import platform

def finddisk():
    print("开始查找电脑所有盘符...")
    a = []
    result = os.popen('wmic logicaldisk get caption')
    print("查询结果：")
    # 返回的结果是一个<class 'os._wrap_close'>对象，需要读取后才能处理
    willfind = False
    context = result.read()
    for line in context.splitlines():
        if willfind == True :
            if line != '':
                print(line.replace(" ",""))
                a.append(line.replace(" ",""))

        willfind = True
    result.close()
    return a # 会返回电脑所有盘符的列表，如['C:', 'D:', 'E:']

def winfindgenshin():
    a = finddisk()
    b = False
    for i in a:
        print('正在查找' + i + "...")
        """
        if b == True:
            continue # 已经找到了就不用继续了
        else:
            willrun = "cd " + i + "\\ && dir yuanshen* /s /b"
            result = os.popen(willrun)
        """
        willrun = "cd /d" + i + "\\ && dir genshin* /s /b"
        result = os.popen(willrun) # 出于稳定性，我决定使用史山代码

        # 如果在查找C，那么就是cd c:\ && dir mhy* /s /b
        # 查找目录下和子目录所有以yuanshen开头的文件
        context = result.read()
        print(context)
        # print(type(context))
        if ("enshin" in context) == True :
            b = True
            # print("b = True")
        result.close()
    if b == True:
        print("你的电脑存在病毒软件原神！！！")
    else:
        print("恭喜，你的电脑不存在病毒软件原神！！！")

import readchar

if platform.system().lower() == 'windows':
    print("系统为Windows，开始运行...")
    winfindgenshin()
    print("按任意键结束...")
    readchar.readchar()
elif platform.system().lower() == 'linux':
    print("按任意键结束...")
    readchar.readchar()
else:
    print("按任意键结束...")
    readchar.readchar()
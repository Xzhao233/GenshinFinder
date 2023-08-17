import os
import platform
import threading
import readchar


class GenshinSearchThread(threading.Thread):
    def __init__(self, disk):
        super().__init__()
        self.disk = disk
        self.result = False

    def run(self):
        if self.is_disk_online():
            self.result = self.search_genshin_virus()
        else:
            print("磁盘 " + self.disk + " 处于脱机状态")

    def is_disk_online(self):
        try:
            willrun = 'cd /d ' + self.disk
            result = os.system(willrun)
            return result == 0
        except Exception as e:
            return False

    def search_genshin_virus(self):
        try:
            willrun = 'cd /d ' + self.disk + ' && dir /s /b yuanshen* '
            result = os.system(willrun)
            return result == 0
        except Exception as e:
            print("搜索 " + self.disk + " 时出现错误：" + str(e))
            return False

def finddisk():
    print("开始查找电脑所有盘符...")
    a = []
    result = os.popen('wmic logicaldisk get caption')
    print("查询结果：")
    context = result.read()
    for line in context.splitlines():
        if line.strip() and len(line.strip()) == 2:
            print(line.strip())
            a.append(line.strip())
    result.close()
    return a

def winfindgenshin():
    disks = finddisk()
    threads = []
    for disk in disks:
        thread = GenshinSearchThread(disk)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    found_virus = any(thread.result for thread in threads)
    if found_virus:
        print("你的电脑存在病毒软件原神！！！")
    else:
        print("恭喜，你的电脑不存在病毒软件原神！！！")

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

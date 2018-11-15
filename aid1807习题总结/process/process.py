from multiprocessing import Pool, Manager
import os
import time


def copyFileTask(name, oldFolderName, newFolderName, queue):
    # print("---start-copy---")
    queue.put(name)
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name, "w")
    # print("---start-copy_name---")

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()


def main():
    # o.获取文件夹的名字
    oldFolderName = input("请输入您要拷贝的文件夹名：")

    # 1.创建一个文件夹
    newFolderName = oldFolderName+"-复件"
    # print(newFolderName)
    os.mkdir(newFolderName)
    print("创建文件夹成功！")
    # 2.获取old文件夹中所有的文件名
    p = os.listdir(oldFolderName)
    # print(p)
    # 3.使用多进程拷贝

    pool = Pool(5)
    queue = Manager().Queue()
    for name in p:
        pool.apply_async(copyFileTask, args=(
            name, oldFolderName, newFolderName, queue))

    num = 0
    allnum = len(p)
    while True:
        queue.get()
        num += 1
        copyRate = num/allnum
        print("\rcopy的进度是：%.2f%%" % (copyRate*100), end="")
        if num == allnum:
            break

    # pool.close()
    # pool.join()

    print("\n已完成copy!")

    '''
    time.sleep(3)
    os.rmdir(newFolderName)
    print("创建的复件文件夹已经删除")
    '''


if __name__ == "__main__":
    main()

'''bug
多次测试中有部分文件，只复制了文件名，内容没有复制，不知道原因
如果文件夹里有文件夹也不会拷贝里面的这个文件夹
'''

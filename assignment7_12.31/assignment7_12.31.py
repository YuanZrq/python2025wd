import os
import sys

# 1.完成包的使用（与上课一致）
import q1

q1.send_m.send()
txt = q1.receive_m.receive()
print(txt)


# 2.完成文件的文本模式的读，写（与上课一致）
def open_r():
    file = open('file2.txt', mode='r', encoding='utf-8')
    text = file.read()
    print(text)
    file.close()


def open_w():
    file = open('file3', mode='w', encoding='utf-8')
    file.write('hello坚持学习')
    file.close()


# 3.完成目录的listdir，getcwd,chdir的使用（与上课一致）
def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)
    print(os.getcwd())
    os.chdir('dir2')
    file = open('file1', 'w', encoding='utf-8')
    file.close()


def change_dir():
    print(os.getcwd())
    os.chdir('dir2')  # 类似于进入这个目录
    print(os.getcwd())


def scan_dir(current_path, width):
    file_list = os.listdir(current_path)  # 得到当前文件夹下的所有文件
    for file in file_list:
        print(' ' * width, file)  # 打印文件名,width代表多少个空格
        new_path = current_path + '/' + file  # 把当前路径和文件名拼接到一起
        if os.path.isdir(new_path):
            scan_dir(new_path, width + 4)


def use_stat(file_path):
    file_info = os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid,
                                                 file_info.st_mode, file_info.st_mtime))
    from time import strftime
    from time import gmtime
    gm_time = gmtime(file_info.st_mtime)
    print(strftime("%Y-%m-%d %H:%M:%S", gm_time))


# 4.完成python的传参练习（与上课一致）
def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf8')
    file.write('hello')
    file.close()


if __name__ == '__main__':
    open_r()
    open_w()
    print('-' * 99)
    change_dir()
    scan_dir('.', 0)
    use_stat('file4')
    print('-' * 99)
    write_hello(sys.argv[1])

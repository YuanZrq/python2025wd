# Q4:写一个模块（命名不要用中文），模块里写3个打印函数，然后另外一个py文件调用该模块，并调用对应模块的函数，同时用一下下面操作
'''
if __name__ == '__main__':
    wd5.print_line()  # 调用函数
'''


def print1():
    print(f'第一个print')


def print2():
    print(f'第二个print')


def print3():
    print(f'第三个print')


def main():
    print1()
    print2()
    print3()


if __name__ == '__main__':
    main()

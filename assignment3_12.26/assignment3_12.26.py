# Q1:有7个整数，其中有3个数出现了两次，1个数出现了一次， 找出出现了一次的那个数。
def q1():
    list1 = [1, 1, 2, 2, 3, 3, 4]
    for i in list1:
        print(f'{i}出现的次数是：{list1.count(i)}')


# Q2:写一个简单的for循环，从1打印到20，横着打为1排
def q2():
    list2 = [x for x in range(1, 21)]
    for i2 in list2:
        print(f'{i2}', end=' ')


# Q3:写一个say_hello函数打印多次hello并给该函数加备注（具体打印几次依靠传递的参数），然后调用say_hello，同时学会快速查看函数备注，及如何跳转到函数实现快捷操作（与上课一致）
def q3_say_hello(times):
    print('hello ' * times)


# Q4:写一个模块（命名不要用中文），模块里写3个打印函数，然后另外一个py文件调用该模块，并调用对应模块的函数，同时用一下下面操作
def q4():
    import ModuleForQ4
    ModuleForQ4.print1()
    ModuleForQ4.print2()
    ModuleForQ4.print3()


# Q5:练习列表基本使用，排序，生成式等各种操作（与上课的代码保持一致）
def q5():
    my_list = [x if x % 2 == 0 else x ** 2 for x in range(10)]
    print('原列表')
    for a in my_list:
        print(f'{a}', end=' ')
    print()
    my_list.append(10)
    print('列表append')
    for b in my_list:
        print(f'{b}', end=' ')
    print()
    my_list.remove(1)
    print('列表remove')
    for c in my_list:
        print(f'{c}', end=' ')
    print()
    my_list.pop()
    print('列表pop')
    for d in my_list:
        print(f'{d}', end=' ')
    print()
    my_list.sort(reverse=True)
    print('列表sortT')
    for e in my_list:
        print(f'{e}', end=' ')


# Q6:有8个整数，其中有3个数出现了两次，2个数出现了一次， 找出出现了一次的那2个数。


if __name__ == '__main__':
    q1()
    print()
    q2()
    print()
    q3_say_hello(5)
    print()
    q4()
    print()
    q5()

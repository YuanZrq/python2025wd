# Q2:自己定义变量赋值不同的数据类型并打印，并使用type
def q2():
    a = 10
    b = 2.5
    c = 'hello'
    d = True
    e = False
    print(a, b, c, d, e)
    print(type(a), type(b), type(c), type(d), type(e))


# Q3:能够将整型转为不同进制，进行输出(与上课一致)
def q3():
    a = 123
    print(bin(a))
    print(oct(a))
    print(hex(a))


# Q4:实现从1到100之间的奇数求和
def q4():
    i = 1
    sum_odd = 0
    while i < 100:
        if i % 2 == 1:
            sum_odd += i
        i += 1
    print(sum_odd)


# Q5:打印九九乘法表(直接百度乘法表图像，与其一致即可)
def q5():
    i = 1
    j = 1
    while i <= 9:
        while j <= i:
            print('%d×%d=%d' % (j, i, i * j), end=' ')
            j += 1
        j = 1
        print('\n')
        i += 1


# Q6:统计一个整数对应的二进制数的1的个数。输入一个整数(可正可负，负数就按64位去遍历即可)，计算出该整数的二进制包含1的个数(使用位运算)
def q6():
    s = int(input('请输入一个整数：'))
    count = 0
    flag = 1
    while flag < 2 ** 64:
        if flag & s:
            count += 1
        flag <<= 1
    print(count)


q2()
print('\n')
q3()
print('\n')
q4()
print('\n')
q5()
print('\n')
q6()

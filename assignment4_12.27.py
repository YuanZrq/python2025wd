# 把今天讲的元组，字典，字符串，集合，函数缺省参数等所有接口基本功能练习一遍，和上课代码保持一致
# 元组
def use_tuple():
    tuple1 = (1, 1, 2, 3, 3, 3)
    print(len(tuple1))
    print(tuple1.count(1))
    print(tuple1.index(3))
    print(tuple1[5])


# 字典
def use_dict():
    dict1 = {'a': 1, 'b': 2}
    print(dict1.setdefault('d', 4))
    dict1['c'] = 3
    print(dict1)
    del dict1['a']
    dict1.pop('b')
    print(dict1)
    dict1['d'] = 2
    print(dict1)
    dict2 = {'d': 4, 'e': 5}
    dict1.update(dict2)
    print(dict1)
    print(dict1['e'])
    for k, v in dict1.items():
        print(f'key {k},value {v}')


# 字符串
def use_str():
    str1 = 'asdf gh jkl'
    print(len(str1))
    print(str1.count('as'))
    print(str1[2])
    print(str1.index('d'))
    print(str1.isdecimal())
    print(str1.islower())
    print(str1.upper())
    print(str1.split())
    print(str1.splitlines())
    print(str1[2:6])


# 集合
def use_set():
    set1 = {'a', 'b', 'c', 'a', 'b', 'e'}
    print(set1)


# 函数，缺省参数
def f(name, age=18):
    print(name, age)


if __name__ == "__main__":
    use_tuple()
    print()
    use_dict()
    print()
    use_str()
    print()
    use_set()
    print()
    f('jkl')
    f('das', 10)

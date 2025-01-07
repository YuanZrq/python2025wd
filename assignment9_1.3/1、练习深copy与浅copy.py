import copy


# 1、练习深copy与浅copy
def shallow_copy():
    """
    浅copy，只复制对应“指针”，传址，指向对象变化会导致浅copy也变
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


def deep_copy():
    """
    深copy，也会复制指向的值，传值，与原对象无关
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


if __name__ == '__main__':
    shallow_copy()
    deep_copy()

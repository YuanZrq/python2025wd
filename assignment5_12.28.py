# 多个缺省参数的传递练习，练习多个缺省参数
def print_info(name, position='', age=18, gender=True):
    if gender:
        gender_text = '男生'
    else:
        gender_text = '女生'
    print('咱班%s%s今年%d岁，是个%s' % (position, name, age, gender_text))


# 多值参数练习，元组，字典的传参拆包练习
def demo(*args, **kwargs):
    print(f'demo{args}')
    print(f'demo{kwargs}')


def demo2(*args, **kwargs):
    demo(*args, **kwargs)
    print(f'demo2{args}')
    print(f'demo2{kwargs}')


# 设计一个类，实例化1个对象，会实现下面两种行为
'''
    一只 黄颜色 的 狗狗 叫 大黄
    •具有  汪汪叫 行为
    •具有  摇尾巴 行为
'''


class Dog:
    def __init__(self, name, color, bio):
        self.name = name
        self.color = color
        self.bio = bio

    def bark(self):
        print(f'{self.name}汪汪叫')

    def tail(self):
        print(f'{self.name}摇尾巴')


if __name__ == "__main__":
    print_info('李明', '班长', 18, True)
    demo2('a', 'b', 1, 4, 7, name='zjkl', age=18)
    yellow = Dog('大黄', '黄颜色', '狗狗')
    yellow.bark()
    yellow.tail()

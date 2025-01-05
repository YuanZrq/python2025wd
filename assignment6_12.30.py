# 1、练习封装案例（和上课保持一致即可）
class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print(f'没有子弹了')
            return
        self.bullet_count -= 1
        print(f'{self.model}发射子弹，剩余{self.bullet_count}发子弹')


class Soldier:
    def __init__(self, name, gun: Gun = None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:
            print(f'{self.name}还没有枪')
            return
        self.gun.add_bullet(30)
        self.gun.shoot()


# 2、练习私有属性和私有方法（和上课保持一致即可）
class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print(f'{self.name}年龄{self.__age}')

    def boy_friend(self):
        self.__secret()


# 3、练习单继承，多重继承案例（和上课保持一致即可）
class Parent:
    def __init__(self, height):
        self.height = height


class Son1(Parent):
    def __init__(self, age, *args):
        self.age = age
        super().__init__(*args)


class Son2(Parent):
    def __init__(self, score, *args):
        self.score = score
        super().__init__(*args)


class Grandson(Son1, Son2):
    def __init__(self, name, *args):
        self.name = name
        super().__init__(*args)


# 4、实现单例模式（和上课保持一致即可）
class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name


# 5、通过try进行异常捕捉，确保输入的内容一定是一个整型数，
# 然后判断该整型数是否是对称数，12321就是对称数，
# 123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常

def q5():
    while True:
        try:
            n = int(input('请输入一个整数：'))
            s = str(n)
            if s == s[::-1]:
                print(f'{n}是对称数')
                break
            else:
                raise Exception(f'{n}不是对称数')
        except ValueError:
            print('你输入的不是整数')
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    M4 = Gun('M4')
    M4.add_bullet(1)
    M4.shoot()
    abbb = Soldier('阿biubiubiu')
    abbb.fire()
    abbb.gun = M4
    abbb.fire()
    print('-' * 100)
    xxx = Women('xxx', 18)
    xxx.boy_friend()
    print('-' * 100)
    xiaoming = Grandson('小明', 18, 98.5, 175)
    print(xiaoming.name)
    print(xiaoming.age)
    print(xiaoming.score)
    print(xiaoming.height)
    print(Grandson.__mro__)
    print('-' * 100)
    player1 = MusicPlayer('七里香')
    player2 = MusicPlayer('东风破')
    print(id(player1))
    print(id(player2))
    print(player1.name)
    print(player2.name)
    print('-' * 99)
    q5()

import random
from operator import itemgetter, attrgetter


# 1、完成二叉树的建树，前序，中序，后序，层序遍历
class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:
    def __init__(self):
        self.root = None
        self.aux_queue = []

    def build_tree(self, node=Node):
        self.aux_queue.append(node)
        if not self.root:
            self.root = node
        else:
            if not self.aux_queue[0].lchild:
                self.aux_queue[0].lchild = node
            else:
                self.aux_queue[0].rchild = node
                self.aux_queue.pop(0)

    def preorder(self, current_node: Node):
        if current_node:
            print(current_node.elem, end=' ')
            self.preorder(current_node.lchild)
            self.preorder(current_node.rchild)

    def inorder(self, current_node: Node):
        if current_node:
            self.inorder(current_node.lchild)
            print(current_node.elem, end=' ')
            self.inorder(current_node.rchild)

    def postorder(self, current_node: Node):
        if current_node:
            self.postorder(current_node.lchild)
            self.postorder(current_node.rchild)
            print(current_node.elem, end=' ')

    def level_order(self):
        aux_queue = []
        aux_queue.append(self.root)
        while aux_queue:
            out_node: Node = aux_queue.pop(0)
            print(out_node.elem, end=' ')
            if out_node.lchild:
                aux_queue.append(out_node.lchild)
            if out_node.rchild:
                aux_queue.append(out_node.rchild)


# 2、完成sorted的练习
my_list = "This is a test string from Andrew".split()
print(my_list)


def change_lower(str_name: str):
    return str_name.lower()


# key可以传递一个比较规则的函数,比较规则发生了改变,key就是给它传递一个函数
# print(sorted(my_list, key=change_lower))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student = Student('john', 'A', 15)
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        new_node = Node(i)
        tree.build_tree(new_node)
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()
    tree.level_order()
    print()
    print('-' * 99)
    my_list.sort(key=change_lower)
    print(my_list)
    print('-' * 50)
    student_tuples = [
        ('jane', 'B', 12),
        ('john', 'A', 15),
        ('dave', 'B', 10),
    ]
    print(sorted(student_tuples, key=lambda x: x[2]))
    print('-' * 50)
    print(sorted(student_objects, key=lambda student: student.age))
    print(sorted(student_tuples, key=itemgetter(0)))
    print(sorted(student_objects, key=attrgetter('age')))
    print(sorted(student_tuples, key=itemgetter(1, 2)))
    print(sorted(student_tuples, key=lambda x: (x[1], -x[2])))
    print(sorted(student_objects, key=attrgetter('grade', 'age'), reverse=True))

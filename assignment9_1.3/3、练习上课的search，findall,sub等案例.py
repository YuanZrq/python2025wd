# 3、练习上课的search，findall,sub等案例
import re

def func():
    """
    search findall sub split
    :return:
    """
    ret = re.search(r"\d+", "阅读次数为 9999,点赞888")
    print(ret.group())
    print('-' * 50)
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)
    print('-' * 50)
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)
    ret = re.sub(r"\d+", lambda x: str(int(x.group()) + 100), "python = 997")
    print(ret)
    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)
    print('-' * 50)
    # sub只替换前两个
    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"

    new_text = re.sub(pattern, replacement, text, count=3)
    print(new_text)


if __name__ == '__main__':
    func()
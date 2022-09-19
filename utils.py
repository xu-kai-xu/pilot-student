from math import sqrt

def is_prime(n):
    """Return a boolean value based upon whether tha argument n is a prime number."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

def say_hi(*names, greeting='Hi', capitalized=False):
    """
    Print a string with a greeting to everyone.
    :param *names: tuple of names to be greeted.
    :param greeting: 'Hi' as default.
    :param capitalized: Whether name should be converted to capitalized before print. False as default.
    :return: None
    """
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f"{greeting}, {name}!")
    return None

if __name__ == '__main__':
    pass
    """
    此处一般放针对这个类或函数编写的测试代码。

    这里的代码当且仅当在命令行直接运行 python 源文件时才会被执行。
    （以 python utils.py 或 python -m utils 的方式运行）。

    当文件被其他源文件引用时该代码不执行（以 import utils 的方式）。
    """
    
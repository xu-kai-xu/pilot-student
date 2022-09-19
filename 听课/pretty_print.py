import keyword

keyword.kwlist

def pprint(cont):
    # 打印列表，使得每行一个列表元素
    for item in cont:
        if item == cont[-1]:
            print(item)
        else:
            print(item+'\n')
if __name__ == '__main__':
    pprint(keyword.kwlist)
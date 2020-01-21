"""对于'r+'来说，如果先读取了内容，再写入的话就变成了追加的模式，如果直接写入内容，就是覆盖了"""


def prime(num):
    """判断素数"""
    end = int(num ** 0.5) + 1
    for i in range(2, end):
        if num % i == 0:
            return False
    return True if num != 1 else False


def main():
    files = (r'..\a.txt', r'..\b.txt', r'..\c.txt')
    fs_list = []
    try:
        for file in files:
            fs_list.append(open(file, 'r+'))
        for factor in range(1, 10000):
            if factor < 100 and prime(factor):
                fs_list[0].write(str(factor) + '\n')
            elif factor < 1000 and prime(factor):
                fs_list[1].write(str(factor) + '\n')
            elif factor < 10000 and prime(factor):
                fs_list[2].write(str(factor) + '\n')
    except IOError as ex:
        print(ex)
        print('写入文件时发生错误')
    finally:
        for f in fs_list:
            f.close()
    print('操作成功')


if __name__ == '__main__':
    main()



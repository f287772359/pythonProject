def add(*args):   #加法
    total = 0
    for val in args:     #将每个变量取出来
        total += val
    return total
print(add(1,3,5,7,9))

def gcd(x,y):         #最大公约数
    (x,y) = (y,x) if x > y else (x,y)
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x,y):
    """最小公倍数"""
    return x * y // gcd(x,y)

def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2,int(num // 2) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


def zfc():
    s1 = 'hello ' * 3
    print(s1)  # hello hello hello
    s2 = 'world'
    s1 += s2
    print(s1)  # hello hello hello world
    print('ll' in s1)  # True
    print('good' in s1)  # False
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    a, b =a, b = 5, 10
    print('{0} * {1} = {2}'.format(a, b, a * b))
    print(f'{a} * {b} = {a * b}')

def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)  # [1, 3, 5, 7, 100]
    # 乘号表示列表元素的重复
    list2 = ['hello'] * 3
    print(list2)  # ['hello', 'hello', 'hello']
    # 计算列表长度(元素个数)
    print(len(list1))  # 5
    # 下标(索引)运算
    print(list1[0])  # 1
    print(list1[4])  # 100
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1])  # 100
    print(list1[-3])  # 5
    list1[2] = 300
    print(list1)  # [1, 3, 300, 7, 100]
    # 通过循环用下标遍历列表元素
    for index in range(len(list1)):
        print(list1[index])
        # 通过for循环遍历列表元素
    for elem in list1:
        print(elem)
        # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
    for index, elem in enumerate(list1):
        print(index, elem)

if __name__ == '__main__':
    main()






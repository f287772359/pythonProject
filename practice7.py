import os
import time
import random
from random import randrange,randint,sample

def led_circle():
    content = '北京欢迎你为你开天辟地......'
    while True:
        #清理屏幕上的输出
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_code = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_code = len(all_code) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_code)
        code += all_code[index]
    return code

def list_max(x):
    num_first = x[0]
    num_second = x[0]
    for index in range(1,len(x)):
        if num_first < x[index]:
            num_second = num_first
            num_first = x[index]
        elif num_second < x[index]:
            num_second = x[index]
    return num_first,num_second

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 ==0

def which_day(year,month,date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

def random_select():
    # 随机选择一组号码
    red_balls = [x for x in range(1,34)]
    selected_balls = []
    selected_balls = sample(red_balls,6)
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls

def display(balls):
    for index,ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|',end=' ')
        print('%02d' % ball,end=' ')
    print()

def lucky_person():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def triple_yh():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

def main():
    # 输出5位密码
    # print(generate_code(5))
    # 输出list中最大的数和第二大的数
    # print(list_max([5,61,12,100,81]))
    # print(which_day(2016, 3, 1))
    # n = int(input('机选几注：'))
    # for _ in range(n):
    #    display(random_select())
    lucky_person()


if __name__ == '__main__':
    main()

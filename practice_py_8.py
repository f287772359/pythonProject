from time import sleep
from math import sqrt

class Student(object):
    # __init__初始化
    # 为学生对象绑定name和age两个属性
    def __init__(self,name,age):
        self.name = name
        self.age =age

    def study(self,course):
        print('%s正在学习%s.' % (self.name,course))

    def watch_movie(self):
        if self.age < 18:
            print('%s看《熊出没》.' % (self.name))
        else:
            print('%s看《鬼吹灯》.' % (self.name))

class Clock(object):
    # 数字时钟

    def __init__(self,hour=0,min=0,second=0):
        self._hour = hour
        self._min = min
        self._second = second

    def run(self):
    # 走字
        self._second += 1
        if self._second == 60:
            self._min += 1
            self._second = 0
            if self._min == 60:
                self._hour += 1
                self._min = 0
                if self._hour == 24:
                    self._hour = 0

    def display(self):
        return '%02d:%02d:%02d' % \
               (self._hour,self._min,self._second)

class Point(object):

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def move_to(self,x,y):
        self.x = x
        self.y = y

    def move_by(self,x,y):
        self.x += x
        self.y += y

    def distance_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' %(str(self.x),str(self.y))


def main():
    # 创建学生对象并指定姓名和年龄
    # stu1 = Student('秋水',24)
    # stu1.study('Pyrhon')
    # stu1.watch_movie()
    # stu2 = Student('大林',16)
    # stu2.study('相声')
    # stu2.watch_movie()
    # clock = Clock(23,59,58)
    # while True:
    #    print(clock.display())
    #    sleep(1)
    #    clock.run()
    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1,2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()

import math
from functools import reduce
import functools
import os
import re
from datetime import datetime, timezone, timedelta


def abs(number):
    if not isinstance(number,(int,float)):
        raise TypeError('bad operand type')
    if number >= 0 :
        return number
    return -number

def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

def quadratic(a, b, c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(b,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    delta = b * b - 4 *a *c
    if delta < 0:
        return
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

def add_l(L = []):
    L.append('end')
    return L

def hanoi(n, a, b, c):
    if n == 1:
        print('%s --> %s' % (a, c))
    else:
        move(n - 1, a, c, b)        #将a上n - 1个圆盘借助c移动到b
        move(1, a, b, c)            #将a上1个圆盘移动到c
        move(n - 1, b, a, c)        #将b上n -1个圆盘借助a移动到c
    return

#把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]

def normalize(name):
    length = len(name)
    strtmp = ''
    i = 0
    while i < length:
        if i == 0:
            strtmp += name[i].upper()
        else:
            strtmp += name[i].lower()
        i = i + 1
    return strtmp

def prod(L):
    def production(a, b):
        return a * b
    return reduce(production,L)

def str2float(s):
    if s == '':
        return None
    def ptindex(s):
        i = 0
        while i < len(s):
            if s[i] == '.':
                return i
            i = i + 1
        return -1
    def lessthan0(s):
        if s[0] == '-':
            return True
        else:
            return False         
    def char2sum(c):
        return {'0':1, '1':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]
    def proc(a,b):
        return 10 * a + b
    if lessthan0(s):
        return -1 * str2float(s[1:len(s)])
    else:
        a , b = 0, 0
        i = ptindex(s)
        if i == -1:
            return reduce(proc,map(char2sum,s))
        else:
            a = reduce(proc,map(char2sum,s[:i]))
            b = reduce(proc,map(char2sum,s[i + 1:len(s)]))
            c = b
            j = len(s) - i - 1
            k = 0
            while k < j:
                c = c * 0.1
                k = k + 1
            return a + c

def is_palindrome(n):
    strtmp = str(n)
    leng = len(strtmp)
    t = leng / 2
    i = 0
    while i < t:
        if(strtmp[i] != strtmp[leng - 1 - i]):
            return False
        i = i + 1
    return True

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

def call(func):
    @functools.wraps(func)
    def wrap(*args, **kv):
        print('begin call')
        func(*args,**kv)
        print('end call')
    return wrap
@call
def now():
    print('wangyang')

def log(text):
   if not callable(text):
       def decorator(func):
           @functools.wraps(func)
           def wrapper(*args, **kw):
               print('%s %s():' % (text, func.__name__))
               return func(*args, **kw)
           return wrapper
       return decorator
   else:
       @functools.wraps(text)
       def wrapper2(*args, **kw):
           print('call %s()' % text.__name__)
           return text(*args, **kw)
       return wrapper2

@log
def now7():
    print('This is output info')

@log("execute")
def now8():
    print('This is output info')

def _hello():
    print('hello world')

class Animal(object):
    __slots__ = ('a', 'b')
    def run(self):
        print('Animal is running')

class Dog(Animal):
    __slots__ = ('c')
    def run(self):
        print('Dog is running')

class Husky(Dog):
    def run(self):
        print('Husky is running')
    
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,(int, float)):
            raise ValueError('width must be int or float')
        if value <=0:
            raise ValueError('width must be > 0')
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not isinstance(value,(int, float)):
            raise ValueError('width must be int or float')
        if value <=0:
            raise ValueError('width must be > 0')
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height

def search_file(p, s):
    for x in os.listdir(p):
        if os.path.isdir(x):
            abs_p = os.path.abspath(p)
            sub_abs_p = os.path.join(abs_p, x)
            search_file(sub_abs_p, s)
        else:
            if x.find(s) != -1:
                print(x)
            else:
                pass
    
def print_dir_l():
    os.system('ls -l .')

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    re_compile = re.compile(r'UTC(\S)(\d+):\d+')
    m = re_compile.match(tz_str)
    h = int(m.group(2))
    if m.group(1) == '+':
        tzinfo = timezone(timedelta(hours=h))
    elif m.group(1) == '-':
        tzinfo = timezone(-timedelta(hours=h))
    else:
        pass
    return dt.replace(tzinfo=tzinfo).timestamp()

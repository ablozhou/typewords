import math
import random
sign2 = ['+', '-', '×', '÷']
sign = ['+', '-', '*', '/']
addsub = ['+', '-']
MIN = 1  # 运算数最小值
MAX = 100  # 运算数最大值
SIGN_LEN = 4  # 算式运算符一般不超过4
'''生成四则混合运算，没有负数和小数'''

# a,b 参与运算的2个数
# s 新参与运算的符号
# form 已经生成的公式
# 返回值：新生成的公式, 运算值


def genform(a, b, s, form):

    fb = b
    s1 = s
    # 为负数时调换a,b和公式
    if s == '-' and a < b:
        a, b = b, a
        fb, form = form, fb
    # 除号需要处理除数为0及不能整除的情况
    elif s == '/':
        s1 = '//'
        if b == 0:
            a, b = b, a
            fb, form = form, fb
        n = a % b
        a -= n
        if n != 0:
            form = f'({form} - {n})'
    f = f'{a} {s1} {b}'
    f1 = f'{form} {s} {fb}'
    return f1, eval(f)


while True:
    formula = ''
    random.choice(sign)
    l = random.randint(2, SIGN_LEN)
    a = random.randint(MIN, MAX)
    f = str(a)
    lasts = ''
    for i in range(l):
        b = random.randint(MIN, MAX)
        s = random.choice(sign)
        if s == '*' or s == '/':
            if lasts == '+' or lasts == '-':
                f = f'({f})'
            elif lasts == '/' and s == '/':
                s = random.choice(addsub)

        lasts = s
        f, a = genform(a, b, s, f)
        print(f)

    formula = f.replace('/', '÷').replace('*', '×')
    print(a)
    ans = input(''.join(formula)+' = ')
    if ans == str(a):
        print("---great!---")
    else:
        print(f'answer should be {a}')

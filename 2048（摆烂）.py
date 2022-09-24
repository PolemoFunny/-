#2022年7月9日08:51:10
#Python

#导入模块
from random import random

#坐标变量
x1y1 = 0
x1y2 = 0
x1y3 = 0
x1y4 = 1
x2y1 = 0
x2y2 = 0
x2y3 = 1
x2y4 = 0
x3y1 = 0
x3y2 = 1
x3y3 = 0
x3y4 = 0
x4y1 = 1
x4y2 = 0
x4y3 = 0
x4y4 = 0

#print(str(x1y1)+'|'+str(x1y2)+'|'+str(x1y3)+'|'+str(x1y4))
#print(' ')
#print(str(x2y1)+'|'+str(x2y2)+'|'+str(x2y3)+'|'+str(x2y4))
#print(' ')
#print(str(x3y1)+'|'+str(x3y2)+'|'+str(x3y3)+'|'+str(x3y4))
#print(' ')
#print(str(x4y1)+'|'+str(x4y2)+'|'+str(x4y3)+'|'+str(x4y4))
    
#函数
def 控制朝向():
    global x1y1
    global x1y2
    global x1y3
    global x1y4
    global x2y1
    global x2y2
    global x2y3
    global x2y4
    global x3y1
    global x3y2
    global x3y3
    global x3y4
    global x4y1
    global x4y2
    global x4y3
    global x4y4
    方向=input('你要向哪移动？')
    #上
    if 方向 == 'w' :
        #第一行
        #第一个
        if x1y1 == 0:
            x1y1 = x1y2
            x1y2 = 0
        #第二个
        if x1y2 == 0:
            if x1y1 == 0:
                x1y1 = x1y3
                x1y3 = 0
            else:
                x1y2 = x1y3
                x1y3 = 0
        #第三个
        if x1y3 == 0:
            if x1y2 == 0:
                if x1y1 == 0:
                    x1y1 = x1y4
                    x1y4 = 0
                else:
                    x1y2 = x1y4
                    x1y4 = 0
            else:
                x1y3 = x1y4
                x1y4 = 0
        #第二行
        #第一个
        if x2y1 == 0:
            x2y1 = x2y2
            x2y1 = 0
        #第二个
        if x2y2 == 0:
            if x2y1 == 0:
                x2y1 = x2y3
                x2y3 = 0
            else:
                x2y2 = x2y3
                x2y3 = 0
        #第三个
        if x2y3 == 0:
            if x2y2 == 0:
                if x2y1 == 0:
                    x2y1 = x2y4
                    x2y4 = 0
                else:
                    x2y2 = x2y4
                    x2y4 = 0
            else:
                x2y3= x2y4
                x2y4 = 0
        #第三行
        #第一个
        if x3y1 == 0:
            x3y1 = x3y2
            x3y2 = 0
        #第二个
        if x3y2 == 0:
            if x3y1 == 0:
                x3y2 = x3y3
                x3y3 = 0
            else:
                x3y1 = x3y3
                x3y3 = 0
        #第三个
        if x3y3 == 0:
            if x3y2 == 0:
                if x3y1 == 0:
                    x3y1 = x3y4
                    x3y4 = 0
                else:
                    x3y2 = x3y4
                    x3y4 = 0
            else:
                x3y1 = x3y4
                x3y4 = 0
        #第四行
        #第一个
        if x4y1 == 0:
            x4y1 = x4y2
            x4y2 = 0
        #第二个
        if x2y1 == 0:
            if x4y1 == 0:
                x4y1 = x4y3
                x4y3 = 0
            else:
                x4y2 = x4y3
                x4y3 = 0
        #第三个
        if x4y3 == 0:
            if x4y2 == 0:
                if x4y1 == 0:
                    x4y1 = x4y4
                    x4y4 = 0
                else:
                    x4y2 = x4y4
                    x4y3 = 0
            else:
                x4y3 = x4y4
                x4y3 = 0
    #右
    elif 方向 == 'd' :
        if x1y1 == 0:
            x1y1 = x1y2
            x1y2 = 0
        if x1y2 == 0:
            if x1y1 == 0:
                x1y1 = x1y3
                x1y3 = 0
            else:
                x1y2 = x1y3
                x1y3 = 0
        if x1y3 == 0:
            if x1y2 == 0:
                if x1y1 == 0:
                    x1y1 = x1y4
                    x1y4 = 0
                else:
                    x1y2 = x1y4
                    x1y4 = 0
            else:
                x1y3 = x1y4
                x1y4 = 0
        if x2y1 == 0:
            x2y1 = x2y2
            x2y1 = 0
        if x2y2 == 0:
            if x2y1 == 0:
                x2y1 = x2y3
                x2y3 = 0
            else:
                x2y2 = x2y3
                x2y3 = 0
        if x2y3 == 0:
            if x2y2 == 0:
                if x2y1 == 0:
                    x2y1 = x2y4
                    x2y4 = 0
                else:
                    x2y2 = x2y4
                    x2y4 = 0
            else:
                x2y3= x2y4
                x2y4 = 0
        if x3y1 == 0:
            x3y1 = x3y2
            x3y2 = 0
        if x3y2 == 0:
            if x3y1 == 0:
                x3y2 = x3y3
                x3y3 = 0
            else:
                x3y1 = x3y3
                x3y3 = 0
        if x3y3 == 0:
            if x3y2 == 0:
                if x3y1 == 0:
                    x3y1 = x3y4
                    x3y4 = 0
                else:
                    x3y2 = x3y4
                    x3y4 = 0
            else:
                x3y1 = x3y4
                x3y4 = 0
        if x4y1 == 0:
            x4y1 = x4y2
            x4y2 = 0
        if x2y1 == 0:
            if x4y1 == 0:
                x4y1 = x4y3
                x4y3 = 0
            else:
                x4y2 = x4y3
                x4y3 = 0
        if x4y3 == 0:
            if x4y2 == 0:
                if x4y1 == 0:
                    x4y1 = x4y4
                    x4y4 = 0
                else:
                    x4y2 = x4y4
                    x4y3 = 0
            else:
                x4y3 = x4y4
                x4y3 = 0
    #下
    elif 方向 == 's' :
        if x1y1 == 0:
            x1y1 = x1y2
            x1y2 = 0
        if x1y2 == 0:
            if x1y1 == 0:
                x1y1 = x1y3
                x1y3 = 0
            else:
                x1y2 = x1y3
                x1y3 = 0
        if x1y3 == 0:
            if x1y2 == 0:
                if x1y1 == 0:
                    x1y1 = x1y4
                    x1y4 = 0
                else:
                    x1y2 = x1y4
                    x1y4 = 0
            else:
                x1y3 = x1y4
                x1y4 = 0
        if x2y1 == 0:
            x2y1 = x2y2
            x2y1 = 0
        if x2y2 == 0:
            if x2y1 == 0:
                x2y1 = x2y3
                x2y3 = 0
            else:
                x2y2 = x2y3
                x2y3 = 0
        if x2y3 == 0:
            if x2y2 == 0:
                if x2y1 == 0:
                    x2y1 = x2y4
                    x2y4 = 0
                else:
                    x2y2 = x2y4
                    x2y4 = 0
            else:
                x2y3= x2y4
                x2y4 = 0
        if x3y1 == 0:
            x3y1 = x3y2
            x3y2 = 0
        if x3y2 == 0:
            if x3y1 == 0:
                x3y2 = x3y3
                x3y3 = 0
            else:
                x3y1 = x3y3
                x3y3 = 0
        if x3y3 == 0:
            if x3y2 == 0:
                if x3y1 == 0:
                    x3y1 = x3y4
                    x3y4 = 0
                else:
                    x3y2 = x3y4
                    x3y4 = 0
            else:
                x3y1 = x3y4
                x3y4 = 0
        if x4y1 == 0:
            x4y1 = x4y2
            x4y2 = 0
        if x2y1 == 0:
            if x4y1 == 0:
                x4y1 = x4y3
                x4y3 = 0
            else:
                x4y2 = x4y3
                x4y3 = 0
        if x4y3 == 0:
            if x4y2 == 0:
                if x4y1 == 0:
                    x4y1 = x4y4
                    x4y4 = 0
                else:
                    x4y2 = x4y4
                    x4y3 = 0
            else:
                x4y3 = x4y4
                x4y3 = 0
    #左
    elif 方向 == 'a':
        if x1y1 == 0:
            x1y1 = x1y2
            x1y2 = 0
        if x1y2 == 0:
            if x1y1 == 0:
                x1y1 = x1y3
                x1y3 = 0
            else:
                x1y2 = x1y3
                x1y3 = 0
        if x1y3 == 0:
            if x1y2 == 0:
                if x1y1 == 0:
                    x1y1 = x1y4
                    x1y4 = 0
                else:
                    x1y2 = x1y4
                    x1y4 = 0
            else:
                x1y3 = x1y4
                x1y4 = 0
        if x2y1 == 0:
            x2y1 = x2y2
            x2y1 = 0
        if x2y2 == 0:
            if x2y1 == 0:
                x2y1 = x2y3
                x2y3 = 0
            else:
                x2y2 = x2y3
                x2y3 = 0
        if x2y3 == 0:
            if x2y2 == 0:
                if x2y1 == 0:
                    x2y1 = x2y4
                    x2y4 = 0
                else:
                    x2y2 = x2y4
                    x2y4 = 0
            else:
                x2y3= x2y4
                x2y4 = 0
        if x3y1 == 0:
            x3y1 = x3y2
            x3y2 = 0
        if x3y2 == 0:
            if x3y1 == 0:
                x3y2 = x3y3
                x3y3 = 0
            else:
                x3y1 = x3y3
                x3y3 = 0
        if x3y3 == 0:
            if x3y2 == 0:
                if x3y1 == 0:
                    x3y1 = x3y4
                    x3y4 = 0
                else:
                    x3y2 = x3y4
                    x3y4 = 0
            else:
                x3y1 = x3y4
                x3y4 = 0
        if x4y1 == 0:
            x4y1 = x4y2
            x4y2 = 0
        if x2y1 == 0:
            if x4y1 == 0:
                x4y1 = x4y3
                x4y3 = 0
            else:
                x4y2 = x4y3
                x4y3 = 0
        if x4y3 == 0:
            if x4y2 == 0:
                if x4y1 == 0:
                    x4y1 = x4y4
                    x4y4 = 0
                else:
                    x4y2 = x4y4
                    x4y3 = 0
            else:
                x4y3 = x4y4
                x4y3 = 0
    else:
        pass
def 显示局面():
    print(str(x1y1)+'|'+str(x1y2)+'|'+str(x1y3)+'|'+str(x1y4))
    print(' ')
    print(str(x2y1)+'|'+str(x2y2)+'|'+str(x2y3)+'|'+str(x2y4))
    print(' ')
    print(str(x3y1)+'|'+str(x3y2)+'|'+str(x3y3)+'|'+str(x3y4))
    print(' ')
    print(str(x4y1)+'|'+str(x4y2)+'|'+str(x4y3)+'|'+str(x4y4))
    
print('2048玩法：回复 w s a d 控制 上 下 左 右')
print('两个相同数字碰撞可得到该两个数字的和')
print('当没有地方可以动时游戏结束；当得到2048时胜利。')
while True:
    显示局面()
    控制朝向()


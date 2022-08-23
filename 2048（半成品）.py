#2022年7月9日08:51:10
#Python

#导入模块
from random import random

#坐标变量（这样搞好像太笨了,但不会改，摆了）
x1y1 = 0
x1y2 = 0
x1y3 = 0
x1y4 = 0
x2y1 = 0
x2y2 = 0
x2y3 = 0
x2y4 = 0
x3y1 = 0
x3y2 = 0
x3y3 = 0
x3y4 = 0
x4y1 = 0
x4y2 = 0
x4y3 = 0
x4y4 = 0

#函数
def 显示局面():
    print(str(x1y1)+'|'+str(x1y2)+'|'+str(x1y3)+'|'+str(x1y4))
    print(' ')
    print(str(x2y1)+'|'+str(x2y2)+'|'+str(x2y3)+'|'+str(x2y4))
    print(' ')
    print(str(x3y1)+'|'+str(x3y2)+'|'+str(x3y3)+'|'+str(x3y4))
    print(' ')
    print(str(x4y1)+'|'+str(x4y2)+'|'+str(x4y3)+'|'+str(x4y4))
    
def 控制朝向:
    方向=input('你要向哪移动？')
    if 方向 == 'N' :
        if x1y1 and x1y2 and x1y3 and x1y4 != 0 :
            pass
    elif 方向 == 'E' :
        if x2y1 and x2y2 and x2y3 and x2y4 != 0 :
            pass
    elif 方向 == 'S' :
        if x3y1 and x3y2 and x3y3 and x3y4 != 0 :
            pass
    elif 方向 == 'W':
        if x4y1 and x4y2 and x4y3 and x4y4 != 0 :
            pass

print('2048玩法：回复 N S E W 控制 上 下 左 右')
print('两个相同数字碰撞可得到该两个数字的和')
print('当没有地方可以动时游戏结束；当得到2048时胜利。')
while True:
    显示局面()
    控制朝向()
#后面的内容在自己的电脑上写，写完后上传

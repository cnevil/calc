#!/usr/bin/env python
# -*- coding: cp936 -*-
# author: 
# coding = UTF-8
# date: 2014.7.13

from __future__ import division
from math import *
from graphics import *
import sys
reload(sys);
sys.setdefaultencoding('UTF-8')


def fxMax(a, b, func):
    x = a
    step = 0.001
    y = []
    while x <= b:
        y.append(eval(func))
        x = x + 0.001
    return max(y)


def fxMin(a, b, func):
    x = a
    step = 0.001
    y = []
    while x <= b:
        y.append(eval(func))
        x = x + 0.001
    return min(y)


# ��ȡXY����
def getX(a, b, func):
    if a < 0 and b < 0:
        xmin = 1.2 * a
        xmax = -0.2 * a
    elif a > 0 and b > 0:
        xmin = -0.2 * a
        xmax = 1.2 * b
    else:
        xmin = 1.2 * a - 1
        xmax = 1.2 * b + 1
    return xmin, xmax


def getY(a, b, func):
    ymin = fxMin(a, b, func)
    ymax = fxMax(a, b, func)
    if ymin < 0 and ymax < 0:
        yMin = 1.2 * ymin
        yMax = -0.2 * ymin
    elif ymin > 0 and ymax > 0:
        yMin = -0.1 * ymin
        yMax = 1.2 * ymax
    else:
        yMin = 1.2 * ymin - 1
        yMax = 1.2 * ymax + 1
    return yMin, yMax


class button:
    def __init__(self, win, center, width, height, label):
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

    def clicked(self, p):
        return self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax


def drawlabel(win, center, face, size, style, label):
    x, y = center.getX(), center.getY()
    a = Text(Point(x, y), label)
    a.setFace(face)
    a.setSize(size)
    a.setStyle(style)
    a.draw(win)


#��ͼ����
def funcdraw(a, b, func):
    win = GraphWin('Draw Function', 550, 550)
    win.setBackground('white')
    #��ȡXY���������ֵ
    xll, xur = getX(a, b, func)
    yll, yur = getY(a, b, func)
    d = min(b - a, yur - yll)
    win.setCoords(xll - 1, yll - 1, xur + 1, yur + 1)
    #����XYO������
    Line(Point(xll, 0.0), Point(xur, 0.0)).draw(win)
    Line(Point(0.0, yll), Point(0.0, yur)).draw(win)
    Text(Point(-0.05 * d, 0.03 * d), 'O').draw(win)
    Text(Point(-0.05 * d, yur - 0.03 * d), 'Y').draw(win)
    Text(Point(xur, 0.03 * d), 'X').draw(win)
    Line(Point(xur, 0.0), Point(xur - 0.04 * d, 0.02 * d)).draw(win)
    Line(Point(xur, 0.0), Point(xur - 0.04 * d, -0.02 * d)).draw(win)
    Line(Point(0.0, yur), Point(-0.02 * d, yur - 0.03 * d)).draw(win)
    Line(Point(0.0, yur), Point(0.02 * d, yur - 0.03 * d)).draw(win)
    #���ƺ�������
    x = a
    step = 0.002 * (b - a)
    while x <= b:
        y = eval(func)
        p0 = Point(x, y)
        p0.draw(win)
        line = Line(Point(x, 0), Point(x, y))
        line.setFill('lightgray')
        line.draw(win)
        x = x + step
    Text(Point(0.7 * xur, 0.7 * yur), 'y=' + func).draw(win)


def diff(a, func):
    x = a - 0.00001
    y1 = eval(func)
    x = a + 0.00001
    y2 = eval(func)
    a = '%0.12f' % ((y2 - y1) / 0.00002)
    return eval(a)


def inte(a, b, func):
    x = a
    step = 0.00001
    sum = 0.0
    while x <= b:
        sum = sum + 0.00001 * eval(func)
        x = x + 0.00001
    a = '%0.12f' % (sum)
    return eval(a)


def suffix(st):
    listopt = [" "]
    listnum = [" "]
    dictopt = {"+": 1, "-": 1, "*": 2, "/": 2, " ": 0, "(": -1, ")": 9}  #�趨���ȼ�
    for i in range(0, len(st)):
        if (differ(st[i]) == 1):  #�жϣ������������
            if (len(listopt)):
                if (dictopt[st[i]] > dictopt[listopt[len(listopt) - 1]]):  #���ȼ���ջ���ߣ���ջ
                    if st[i] == ")":
                        while (1):
                            tmp = listopt.pop()
                            if tmp == "(":
                                break
                            else:
                                listnum.append(tmp)
                                listnum.append(" ")
                    else:
                        listopt.append(st[i])

                else:  #���st[i]���ȼ���ջ���ͣ�optջ�����ηŵ�num�У�Ȼ���ٰ�st[i]��optջ  
                    if st[i] == "(":   #���ȼ�����ջ��Ԫ�صģ������� �Ӽ��˳���Ҳ������"("��������� "("�� ֱ����ջ  
                        listopt.append(st[i])
                    else:
                        while (dictopt[st[i]] < dictopt[listopt[len(listopt) - 1]] and len(listopt) != 0):  #�������� �Ӽ��˳�
                            tmp = listopt.pop()
                            listnum.append(tmp)
                            listnum.append(" ")  #�����֮��ӿո񣬷���print cnt_string:�� 1.2 5 6 ** 57 14 - + �� 
                        listopt.append(st[i])
        else:   #��������Ĳ�����������numջ  
            listnum.append(st[i])
    while (len(listopt)):   #optջ ���ηŵ� numջ  
        listnum.append(" ")  #�����ǰ��ӿո񣬷���print cnt_string:�� 1.2 5 6 * * 57 14-+ �� 
        listnum.append(listopt.pop())
    return listnum


#�ж�����������ǲ�������  
def differ(elem):
    if elem == "+" or elem == "-" or elem == "*" or elem == "/" or elem == "(" or elem == ")":
        return 1
    else:
        return 0


#�����ַ������б�ȥ������Ҫ�Ŀո�
def order(st):
    suffix_list = []
    tmp_list = suffix(st)
    last_string = "".join(tmp_list)
    cnt_string = last_string.replace("  ", " ")
    cnt_string = cnt_string[1:len(cnt_string) - 1]   #�ո�ȥͷȥβ  
    cnt_list_tmp = cnt_string.split(" ")
    for i in cnt_list_tmp:
        if i != "":
            suffix_list.append(i)
    return suffix_list


#ʵ������switch-case ���ܣ�
def calc(type, x, y):
    calculation = {"+": lambda x, y: ( eval(x) + eval(y)),
                   "*": lambda x, y: ( eval(x) * eval(y)),
                   "-": lambda x, y: ( eval(x) - eval(y)),
                   "/": lambda x, y: ( eval(x) / eval(y))
    }
    return calculation[type](x, y)


#usage :result1 = calc('+',3,6)

#���㣺 
def count(suffix_list):
    tmp_list = []
    for i in suffix_list:
        if not differ(i):
            tmp_list.append(i)
        else:
            tmp1 = tmp_list.pop()
            tmp2 = tmp_list.pop()
            tmp3 = calc(i, str(tmp2), str(tmp1))
            tmp_list.append(tmp3)
    return tmp_list[0]

#�����ַ����Է���ջ����
def strdeal(s):
    i=j=k=0
    List_d =[]
    while j< len(s):
        if '0'<=s[j]<='9':
            j+=1
        elif 'A'<=s[j]<='z':
            if '0'<=s[j-1]<='9':
                List_d.append(s[i:j])
            List_d.append(s[j:j+3])
            j+=3
            i=j
        elif '('<=s[j]<='/':
            if s[j]!='.':
                if '0'<=s[j-1]<='9':
                    List_d.append(s[i:j])
                List_d.append(s[j:j+1])
                i=j+1
            j+=1
    List_d.append(s[i:j])
    while k<len(List_d):
        if List_d[k]=='sin':
            List_d[k]=str(sin(eval(List_d[k+1])))
            del List_d[k+1]
        elif List_d[k]=='cos':
            List_d[k]=str(cos(eval(List_d[k+1])))
            del List_d[k+1]
        elif List_d[k]=='tan':
            List_d[k]=str(tan(eval(List_d[k+1])))
            del List_d[k+1]
        k+=1
    s = ' '.join(List_d)
    return s

#eval main
def eval0(s):
    s=strdeal(s)
    suffix_list = order(s)
    answer = count(suffix_list)
    return answer


#???
def FuncGraph():
    win = GraphWin(u"Python\u8BA1\u7B97\u5668", 300, 490)
    win.setCoords(0.0, 0.0, 10, 13.6)
    bg = Rectangle(Point(0.4, 11.9), Point(9.5, 13.2))
    bg.setFill('white')
    bg.draw(win)
    show = Text(Point(5, 12.7), "")
    show.draw(win)
    
    drawlabel(win, Point(1.3, 11.6), 'arial', 9, 'bold italic', u'\u62D3\u5C55\u529F\u80FD:')
    drawlabel(win, Point(1.3, 10.8), 'arial', 8, 'bold italic', 'Low')
    E1 = Entry(Point(2.3, 10.8), 3)
    E1.draw(win)
    drawlabel(win, Point(3.8, 10.8), 'arial', 8, 'bold italic', 'Up')
    E2 = Entry(Point(4.8, 10.8), 3)
    E2.draw(win)
    bDraw = button(win, Point(1.9, 9.8), 1.9, .9, u"\u7ED8\u56FE")
    bInt = button(win, Point(4.4, 9.8), 1.9, .9, u"\u79EF\u5206")
    drawlabel(win, Point(1.1, 8.6), 'arial', 8, 'bold italic', 'X =')
    E3 = Entry(Point(2.2, 8.6), 4)
    E3.draw(win)
    bDiff = button(win, Point(4.4, 8.6), 1.9, .9, u"\u6C42\u5BFC")
    drawlabel(win, Point(5, 7.9), 'arial', 8, 'bold italic',
              '-------------------------------------------------------------------------')
    drawlabel(win, Point(1.3, 7.4), 'arial', 9, 'bold italic', u'\u57FA\u672C\u529F\u80FD:')
    
    b1 = button(win, Point(1, 2.1), 1.2, 1.2, "1")
    b2 = button(win, Point(2.5, 2.1), 1.2, 1.2, "2")
    b3 = button(win, Point(4, 2.1), 1.2, 1.2, "3")
    b4 = button(win, Point(1, 3.6), 1.2, 1.2, "4")
    b5 = button(win, Point(2.5, 3.6), 1.2, 1.2, "5")
    b6 = button(win, Point(4, 3.6), 1.2, 1.2, "6")
    b7 = button(win, Point(1, 5.1), 1.2, 1.2, "7")
    b8 = button(win, Point(2.5, 5.1), 1.2, 1.2, "8")
    b9 = button(win, Point(4, 5.1), 1.2, 1.2, "9")
    bX = button(win, Point(1, 0.6), 1.2, 1.2, " X")
    b0 = button(win, Point(2.5, 0.6), 1.2, 1.2, "0")
    bDot = button(win, Point(4, 0.6), 1.2, 1.2, ".")

    bPi = button(win, Point(5.5, 2.1), 1.2, 1.2, "Pi")
    bE = button(win, Point(5.5, 0.6), 1.2, 1.2, "e")
    bBran1 = button(win, Point(5.5, 5.1), 1.2, 1.2, "(")
    bBran2 = button(win, Point(5.5, 3.6), 1.2, 1.2, ")")
    bPlus = button(win, Point(7.5, 5.1), 1.2, 1.2, "+")
    bMin = button(win, Point(7.5, 3.6), 1.2, 1.2, "-")
    bMul = button(win, Point(7.5, 2.1), 1.2, 1.2, "*")
    bDiv = button(win, Point(7.5, 0.6), 1.2, 1.2, "/")
    bDel = button(win, Point(9, 5.1), 1.2, 1.2, "Del")
    bAC = button(win, Point(9, 3.6), 1.2, 1.2, "AC")
    bEqu = button(win, Point(9, 1.35), 1.2, 2.7, "=")

    bPower = button(win, Point(7.5, 6.5), 1.2, 0.9, "^")
    bSqrt = button(win, Point(9, 6.5), 1.2, .9, "sqrt")
    bsin = button(win, Point(1.4, 6.5), 1.9, .9, "sin")  #sin
    bcos = button(win, Point(3.4, 6.5), 1.9, .9, "cos")  #cos
    btan = button(win, Point(5.4, 6.5), 1.9, .9, "tan")  #tan

    bEsc = button(win, Point(9.8, 13.3), .4, .4, "X")

    IsNewOper=0
    p = win.getMouse()
    while not bEsc.clicked(p):
        try:
            p = win.getMouse()
            if IsNewOper == 1:
                show.setText('')
                IsNewOper = 0
            if b0.clicked(p):
                s = show.getText()
                s = s + "0"
                show.setText(s)
                show.setSize(20)


            elif b1.clicked(p):
                s = show.getText()
                s = s + '1'
                show.setText(s)
                show.setSize(20)

            elif b2.clicked(p):
                s = show.getText()
                s = s + '2'
                show.setText(s)
                show.setSize(20)

            elif b3.clicked(p):
                s = show.getText()
                s = s + '3'
                show.setText(s)
                show.setSize(20)

            elif b4.clicked(p):
                s = show.getText()
                s = s + '4'
                show.setText(s)
                show.setSize(20)

            elif b5.clicked(p):
                s = show.getText()
                s = s + '5'
                show.setText(s)
                show.setSize(20)

            elif b6.clicked(p):
                s = show.getText()
                s = s + '6'
                show.setText(s)
                show.setSize(20)

            elif b7.clicked(p):
                s = show.getText()
                s = s + '7'
                show.setText(s)
                show.setSize(20)

            elif b8.clicked(p):
                s = show.getText()
                s = s + '8'
                show.setText(s)
                show.setSize(20)


            elif b9.clicked(p):
                s = show.getText()
                s = s + '9'
                show.setText(s)
                show.setSize(20)

            elif bMul.clicked(p):
                s = show.getText()
                s = s + '*'
                show.setText(s)
                show.setSize(20)

            elif bDiv.clicked(p):
                s = show.getText()
                s = s + '/'
                show.setText(s)
                show.setSize(20)

            elif bPlus.clicked(p):
                s = show.getText()
                s = s + '+'
                show.setText(s)
                show.setSize(20)

            elif bMin.clicked(p):
                s = show.getText()
                s = s + '-'
                show.setText(s)
                show.setSize(20)

            elif bAC.clicked(p):
                s = ""
                show.setText(s)
                show.setSize(20)

            elif bPi.clicked(p):
                s = show.getText()
                s = s + 'pi'
                show.setText(s)
                show.setSize(20)


            elif bE.clicked(p):
                s = show.getText()
                s = s + 'e'
                show.setText(s)
                show.setSize(20)

            elif bEqu.clicked(p):
                ans = eval0(show.getText())
                show.setText(ans)
                show.setSize(20)
                IsNewOper=1


            elif bBran1.clicked(p):
                s = show.getText()
                s = s + '('
                show.setText(s)
                show.setSize(20)

            elif bBran2.clicked(p):
                s = show.getText()
                s = s + ')'
                show.setText(s)
                show.setSize(20)

            elif bPower.clicked(p):
                s = show.getText()
                s = s + '**'
                show.setText(s)
                show.setSize(20)

            elif bSqrt.clicked(p):
                s = show.getText()
                s = s + 'sqrt('
                show.setText(s)
                show.setSize(20)

            elif bsin.clicked(p):
                s = show.getText()
                s = s + 'sin'
                show.setText(s)
                show.setSize(20)

            elif bcos.clicked(p):
                s = show.getText()
                s = s + 'cos'
                show.setText(s)
                show.setSize(20)

            elif btan.clicked(p):
                s = show.getText()
                s = s + 'tan'
                show.setText(s)
                show.setSize(20)

            elif bDel.clicked(p):
                s = show.getText()
                if s != "Math Error!":
                    s = s[:-1]
                    show.setText(s)
                    show.setSize(20)

            elif bDot.clicked(p):
                s = show.getText()
                s = s + '.'
                show.setText(s)
                show.setSize(20)

            elif bX.clicked(p):
                s = show.getText()
                s = s + 'x'
                show.setText(s)
                show.setSize(20)

            elif bDraw.clicked(p):
                s = show.getText()
                funcdraw(eval(E1.getText()), eval(E2.getText()), s)

            elif bInt.clicked(p):
                s = show.getText()
                a = inte(eval(E1.getText()), eval(E2.getText()), s)
                show.setText(str("%0.2f" % a))
                show.setSize(20)

            elif bDiff.clicked(p):
                s = show.getText()
                a = diff(eval(E3.getText()), s)
                show.setText(str("%0.2f" % a))
                show.setSize(20)


        except:
            show.setText("Math Error!")
            show.setSize(20)

    win.close()


FuncGraph()
    





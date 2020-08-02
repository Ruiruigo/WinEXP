# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 17:05
# @Author  : Ruirui
# @File    : WinEXP.py
# @Software: PyCharm

import re, sys

def openMS():
    MSdata, MSOSdata = {}, {}
    with open('MS', 'r') as t:
        for i in t.read().split('\n'):
            MSdata[i.split('\t')[0]] = 'KB{}'.format(i.split('\t')[1])

    with open('MSOS', 'r') as t:
        MSOS = t.read().replace('\t', '>').split('\n')
        for i in MSOS:
            MSOSdata[i.split('>')[0]] = [j for j in i.split('>')[1:] if j not in '']

    return MSdata, MSOSdata


def Systeminfo(systeminfo):
    def newOS():
        if re.search('\d+', os):
            newos = 'Win' + re.search('\d+', os).group()
            return newos
        elif re.search('[Xx][Pp]', os):
            newos = re.search('[Xx][Pp]', os).group()
            return newos
        elif re.search('[Vv][Ii][Ss][Tt][Aa]]', os):
            newos = re.search('[Xx][Pp]', os).group()
            return newos
    try:
        os = re.search('Microsoft Windows.*', systeminfo).group()
        newWin = newOS()
    except:
        os = '未查询到Windows版本'
        newWin = ''

    KBs = re.findall('KB\d+', systeminfo)
    return newWin, KBs, os


def echo(systeminfo):
    MSIDS = []
    s1, s2, os = Systeminfo(systeminfo)
    if s1 and str(s2) not in '':
        o1, o2 = openMS()
        KBs = [i for i in o1.values()]
        newKBs = [i for i in KBs if i not in s2]

        def getkey(z):
            for i in o1:
                if z in o1[i]:
                    return i

        for i in newKBs:
            try:
                if s1 in o2[getkey(i)]:
                    MSIDS.append(getkey(i))
            except:
                continue

    return MSIDS, os


if __name__=='__main__':
    try:
        path = sys.argv[1]
    except:
        print('使用: python3 WinEXP.py <systeminfo 路径>')
        sys.exit()
    with open(path, 'r') as t:
        systeminfo = t.read()
    exp, os = echo(systeminfo)
    print('服务器系统版本：{}\nEXP列表：{}'.format(os, exp))
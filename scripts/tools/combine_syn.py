#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

__author__ = 'congzicun'
# 格式化同义词词典
# 将feature替换为同义词


def load(file_path):
    syn_dic = {}
    lns = [ln.decode('utf-8').strip() for ln in open(file_path)]
    for ln in lns:
        kws = ln.split(' ')
        for kw in kws:
            syn_dic[kw] = kws[0]
    return syn_dic


def output_syndic(syndic):
    for kw, syn in syndic.items():
        print kw.encode('utf-8'), syn.encode('utf-8')


if __name__ == '__main__':
    syndic = load(sys.argv[1])
    output_syndic(syndic)

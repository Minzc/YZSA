#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'congzicun'


def load_corpus(file_path):
    lns = [ln.decode('utf-8').strip() for ln in open(file_path).readlines()]
    return lns


def load_idf():
    idf = {}
    for ln in open('resource/idf.txt').readlines():
        kw, value = ln.decode('utf-8').strip().split(' ')
        idf[kw] = float(value)
    return idf


def load_dic():
    total_dic = {kw.decode('utf-8').strip() for kw in
                 open('/Users/congzicun/Yunio/pycharm/YZKnowl/dictionary/real_final_dic.txt').readlines()}
    return total_dic


def load_stopdic():
    stop_dic = [ln.strip().decode('utf-8') for ln in
                open('/Users/congzicun/Yunio/pycharm/YZKnowl/dictionary/stopwords.txt').readlines()]
    return stop_dic
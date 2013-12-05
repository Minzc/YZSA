#!/usr/bin/python
# -*- coding: utf-8 -*-
import operator
import sys

__author__ = 'congzicun'


def load_idf(file_path):
    lns = [ln.decode('utf-8') for ln in open(file_path)]
    idf_dic = {}
    for ln in lns:
        kw, score = ln.split(' ')
        idf_dic[kw] = score
    return idf_dic


def load_tf(file_path):
    lns = [ln.decode('utf-8') for ln in open(file_path)]
    tf_dic = {}
    for ln in lns:
        kw, score = ln.split(' ')
        tf_dic[kw] = score
    return tf_dic


def cal_tfidf(tf_dic, idf_dic):
    tfidf = {}
    for kw, score in tf_dic.item():
        tfidf[kw] = score * idf_dic.get(kw, 0)

    std_tfidf = sorted(tfidf.iteritems(), key=operator.itemgetter(1))
    return std_tfidf[:10000]


def output_tfidf(tfidf):
    for kw, score in tfidf:
        print kw.encode('utf-8'), score


if __name__ == '__main__':
    idf_dic = load_idf(sys.argv[1])
    tf_dic = load_tf(sys.argv[2])
    std_tfidf = cal_tfidf(tf_dic, idf_dic)
    output_tfidf(std_tfidf)
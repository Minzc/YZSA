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
        idf_dic[kw] = float(score)
    return idf_dic


def load_tf(file_path):
    lns = [ln.decode('utf-8') for ln in open(file_path)]
    tf_dic = {}
    for ln in lns:
        kw, score = ln.split(' ')
        tf_dic[kw] = float(score)
    return tf_dic


def cal_tfidf(tf_dic, idf_dic):
    tfidf = {}
    for kw, score in tf_dic.items():
        tfidf[kw] = float(score) * idf_dic.get(kw, 0.0)

    std_tfidf = sorted(tfidf.iteritems(), key=operator.itemgetter(1), reverse=True)
    return std_tfidf[:10000]


def output_tfidf(tfidf, filepath):
    f_writer = open(filepath, 'w')
    for kw, score in tfidf:
        if len(kw) == 1 or kw.encode('utf-8').isalpha():
            print kw.encode('utf-8')
            continue

        f_writer.write(kw.encode('utf-8') + '\t' + str(score) + '\n')


if __name__ == '__main__':
    idf_dic = load_idf(sys.argv[1])
    tf_dic = load_tf(sys.argv[2])
    std_tfidf = cal_tfidf(tf_dic, idf_dic)
    output_tfidf(std_tfidf, sys.argv[3])
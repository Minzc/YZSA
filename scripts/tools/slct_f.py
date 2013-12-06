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
    stop_dic = load_stop()
    lns = [ln.decode('utf-8') for ln in open(file_path)]
    tf_dic = {}
    for ln in lns:
        kw, score = ln.split(' ')
        if kw not in stop_dic:
            tf_dic[kw] = float(score)
    return tf_dic


def load_sentidic(file_path):
    sent_dic = {ln.decode('utf-8').split('\t')[0] for ln in open(file_path)}
    return sent_dic


def cal_tfidf(tf_dic, idf_dic):
    tfidf = {}
    for kw, score in tf_dic.items():
        tfidf[kw] = float(score) * idf_dic.get(kw, 0.0)

    std_tfidf = sorted(tfidf.iteritems(), key=operator.itemgetter(1), reverse=True)
    return std_tfidf, tfidf


def select_f(senti_dic, std_tfidf, tfidf):
    valid_f = set()
    print 'select feature'
    for kw in senti_dic:
        if kw in tfidf and not kw.encode('utf-8').isalpha():
            valid_f.add(kw)
    print '#' * 10
    for kw, score in std_tfidf:
        if len(kw) == 1 or kw.encode('utf-8').isalpha():
            continue
        valid_f.add(kw)
        if len(valid_f) > 10000:
            break
    return valid_f


def output_tfidf(sentidic, filepath):
    f_writer = open(filepath, 'w')
    for kw in sentidic:
        f_writer.write(kw.encode('utf-8') + '\n')


def load_stop():
    stop_dic = {ln.decode('utf-8').strip() for ln in open('resource/stopwords.txt').readlines()}
    return stop_dic


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print "<idf> <tf> <sentidic> <output path>"
        sys.exit(-1)
    idf_dic = load_idf(sys.argv[1])
    tf_dic = load_tf(sys.argv[2])
    senti_dic = load_sentidic(sys.argv[3])
    std_tfidf, tfidf = cal_tfidf(tf_dic, idf_dic)
    senti_dic = select_f(senti_dic, std_tfidf, tfidf)
    output_tfidf(senti_dic, sys.argv[4])
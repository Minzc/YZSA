#!/usr/bin/python
# -*- coding: utf-8 -*-
import operator
import re

import nltk

from scripts.util import file_loader, kw_util


__author__ = 'congzicun'


def change_doc(file_name, polarity):
    f_writer = open(file_name + '_changed.txt', 'w')
    idf = file_loader.load_idf()
    corpus = load_copus(file_name)
    stop_dic = file_loader.load_stopdic()
    dictionary = file_loader.load_dic()
    for ln in corpus:
        phrases = '.'.join(extract_keyphrase(ln, idf, stop_dic, dictionary))
        f_writer.write(polarity + '\t' + phrases.encode('utf-8') + '\t' + ln.encode('utf-8') + '\n')
    f_writer.close()


def extract_keyphrase(ln, idf, stop_dic, dictionary):
    sentences = re.split(r'[!.?…~;"#:—]', kw_util.punc_replace(ln))
    tfidf = cal_tfidf(ln, dictionary, stop_dic, idf)
    sentnc_scores = {}
    for sentence in sentences:
        if len(sentence.strip()) > 2:
            sentnc_scores[sentence] = cal_sntnc_scr(sentence, dictionary, tfidf)
    top_ten = [tup[0] for tup in sorted(sentnc_scores.items(), key=operator.itemgetter(1), reverse=True)[:10]]
    if top_ten is not None:
        top_ten.extend(sentences[:3])
        top_ten.extend(sentences[-3:])
        print len(top_ten)
    return top_ten


def cal_sntnc_scr(sentence, dic, tfidf):
    kws = seg(sentence, dic)
    score = 0
    for kw in kws:
        score += tfidf.get(kw, 0)
    return float(score) / float(len(kws) + 1)


def cal_tfidf(ln, dictionary, stop_dic, idf):
    kwcounter = nltk.FreqDist()
    for kw in seg(ln, dictionary):
        if kw not in stop_dic and not kw.encode('utf-8').isalnum():
            kwcounter.inc(kw)
    tfidf = {}
    for kw, v in kwcounter.items():
        tfidf[kw] = v * idf.get(kw, 15.5312024064)
    return tfidf


def seg(ln, dic):
    kwposes = kw_util.backward_maxmatch(ln, dic, 100, 1)
    kws = []
    for kwpos in kwposes:
        kws.append(ln[kwpos[0]:kwpos[1]])
    return kws


def load_copus(file_name):
    return [ln.decode('utf-8').strip() for ln in open(file_name).readlines()]



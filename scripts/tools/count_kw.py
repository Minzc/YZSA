#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

__author__ = 'congzicun'
import nltk


def count_kw(file_path):
    f_reader = open(file_path)
    counter = nltk.FreqDist()
    for ln in f_reader:
        segs = ' '.join(ln.decode('utf-8').strip().split()[1:]).split(' ')
        for seg in segs:
            counter.inc(seg)
    return counter


def output_counter(counter):
    for k, v in counter.items():
        print k.encode('utf-8')


if __name__ == '__main__':
    counter = count_kw(sys.argv[1])
    output_counter(counter)
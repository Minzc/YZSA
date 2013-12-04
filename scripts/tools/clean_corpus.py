#!/usr/bin/python
# -*- coding: utf-8 -*-
from scripts.util import file_loader
from scripts.util import kw_util
__author__ = 'congzicun'


def rm_pos(file_path):
    lns = file_loader.load_corpus(file_path)
    for ln in lns:
        wds = ln.split(' ')
        tw = ''
        for wd in wds:
            tw += wd.split('/')[0]

        print kw_util.punc_replace(tw).encode('utf-8')


if __name__ == '__main__':
    rm_pos('/Users/congzicun/Downloads/dataset_619757/619757/2_simplifyweibo.txt')
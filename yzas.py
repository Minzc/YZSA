#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from scripts.tools import count_kw, gen_matrix

__author__ = 'congzicun'

if __name__ == '__main__':
    if sys.argv[1] == 'count':
        counter = count_kw.count_kw(sys.argv[2])
        count_kw.output_counter(counter)
    elif sys.argv[1] == 'gen':
        gen_matrix.gen_matrix(sys.argv[2])

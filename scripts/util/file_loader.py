#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'congzicun'


def load_corpus(file_path):
    lns = [ln.decode('utf-8').strip() for ln in open(file_path).readlines()]
    return lns
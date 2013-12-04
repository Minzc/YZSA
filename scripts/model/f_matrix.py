#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'congzicun'
import numpy


class feature:
    f_wd = {}

    def load_feature(self, file_path='resource/feature.txt'):
        f_reader = open(file_path)
        num = 0
        for ln in f_reader:
            if ln.startswith('#'):
                continue
            f = ln.decode('utf-8').strip()
            feature.f_wd[f] = num
            num += 1


class vec:
    def __init__(self, ln, dimension, label):
        self.label = label
        self.f_vec = numpy.zeros(dimension)
        words = ln.split(' ')
        for word in words:
            self.f_vec[feature.f_wd[word]] += 1
        self.f_vec = self.f_vec.astype('int64').astype('S10')

    def to_str(self):
        vec_str = self.label
        for index, value in enumerate(self.f_vec):
            if int(value) > 0:
                vec_str = vec_str + ' ' + str(index) + ':' + str(int(value))
        return vec_str


class matrix:
    def __init__(self, f_file_path='resource/feature.txt'):
        self.feature = feature()
        self.feature.load_feature(f_file_path)

    def gen_matrix(self, file_path):
        self.f_matrix = []
        dimension = len(feature.f_wd)
        f_reader = open(file_path)
        for ln in f_reader:
            label = ln.decode('utf-8').strip().split('\t')[0]
            ln = ' '.join(ln.decode('utf-8').strip().split()[1:])
            f_vec = vec(ln, dimension, label)
            self.f_matrix.append(f_vec)
        return self.f_matrix

    def output_matrix(self):
        for vec in self.f_matrix:
            print vec.to_str().encode('utf-8')
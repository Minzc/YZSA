#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import operator

__author__ = 'congzicun'


def extrct_svm_f(file_path, out_put_file):
    f_reader = open(file_path)
    svm_valid_feature = {}
    for ln in f_reader:
        feature, score = ln.strip().decode('utf-8').split('\t')
        if float(score) != 0:
            svm_valid_feature[feature] = abs(float(score))

    svm_valid_feature = sorted(svm_valid_feature.items(), operator.itemgetter(1), reverse=True)

    f_writer = open(out_put_file, 'w')
    for feature in svm_valid_feature:
        f_writer.write(feature[0].encode('utf-8') + '\t' + feature[1] + '\n')
    f_writer.close()


def extract_bigram(feature_file, ifile_path):
    features = set()
    for ln in open(feature_file).readlines():
        features.add(ln.strip().decode('utf-8'))

    f_reader = open(ifile_path)
    valid_pairs = []
    for ln in f_reader:
        kwpair, count = ln.strip().decode("utf-8").split('\t')
        kw1, kw2 = kwpair.split('$')
        if kw1 in features or kw2 in features:
            valid_pairs.append(kwpair)

    f_writer = open(ifile_path + '.output', 'w')
    for valid_pair in valid_pairs:
        f_writer.write(valid_pair)
    f_writer.close()


if __name__ == '__main__':
    if sys.argv[1] == '--help':
        print 'ex <input file> <output file>'
        sys.exit(-1)
    if sys.argv[1] == 'ex':
        extrct_svm_f(sys.argv[2], sys.argv[3])
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from scripts.model.f_matrix import matrix


__author__ = 'congzicun'


def gen_matrix(file_path):
    matrix_obj = matrix()
    matrix_obj.gen_matrix(file_path)
    matrix_obj.output_matrix()


if __name__ == '__main__':
    gen_matrix(sys.argv[1])

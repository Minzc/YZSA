#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys

__author__ = 'congzicun'


def load_copus(file_name):
    return [ln.decode('utf-8').strip().replace('\r', '.').replace('\n', '.').replace('\t', '.') for ln in
            open(file_name).readlines()]


def get_content(js_ln):
    json_obj = json.loads(js_ln)
    return json_obj['text'].strip().replace('\r', '.').replace('\n', '.').replace('\t', '.')


if __name__ == '__main__':
    lns = load_copus(sys.argv[1])
    ln_num = int(sys.argv[2])
    f_writer = open(sys.argv[1] + '_text.txt', 'w')
    for ln in lns[:ln_num]:
        f_writer.write(get_content(ln).encode('utf-8') + '\n')
    f_writer.close()
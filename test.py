#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'module test'

from function import search_file
from function import print_dir_l
import pickle

p = {'a':1,'b':2}
print(p)
s = pickle.dumps(p)
print(s)
p1 = pickle.loads(s)
print(p1)






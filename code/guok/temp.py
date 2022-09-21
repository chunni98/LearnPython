#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# \File        : ./code/guok/learn-oop2.py
# \Author      : chunni
# \Email       : shachi1758@outlook.com
# \CreateTime  : 2022-09-18 19:59:03
# \Version     : 0.1.0
# \Brief       :
# \Log         :

# Chain().users('michael').repos
# /users/michael/repos

class Chain(object):

    def __init__(self, path=''):
        self._path = path
        
    def __call__(self,user_name=''):
        return Chain('%s/%s' % (self._path, user_name))

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().users('michael').repos)
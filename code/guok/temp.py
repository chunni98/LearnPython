#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# \File        : ./code/guok/learn-oop2.py
# \Author      : chunni
# \Email       : shachi1758@outlook.com
# \CreateTime  : 2022-09-18 19:59:03
# \Version     : 0.1.0
# \Brief       :
# \Log         :


# 负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type) -> None:
        self.__name = name
        self.__column_type = column_type
    
    def __str__(self) -> str:
        return "<%s:%s>" % (self.__class__.__name__, self.__name)

class StringField(Field):
    def __init__(self) -> None:
        pass
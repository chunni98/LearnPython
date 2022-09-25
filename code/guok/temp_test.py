#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#\File        : temp_test.py
#\Author      : chunni
#\Email       : shachi1758@outlook.com
#\CreateTime  : 2022-09-25 22:04:58
#\Version     : 0.1.0
#\Brief       : 
#\Log         :

import unittest
from temp import Student

class TestTemp(unittest.TestCase):

    def test_init(self):
        stu = Student("karl", 13, 32.3)
        self.assertEqual(stu.name, "karl")
        self.assertEqual(stu.age, 13)
        self.assertEqual(stu.score,32.3)

    def test_setter(self):
        stu = Student()
        stu.name = "dora"
        self.assertEqual(stu.name, "dora")
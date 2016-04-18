# -*- coding: utf-8 -*-

"""
@author : Gavin / hln3875
@create time: 2016/4/11 21:37
"""


class App(object):

    def __init__(self):
        self.InitEncode()

    def InitEncode(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')
        print "InitEncode -- utf8"

    def Init(self):
        pass

    def Run(self):
        pass


# -*- coding: utf-8 -*-

"""
@author : Gavin / hln3875
@create time: 2016/4/11 21:45
"""
import sys
import os
import msvcrt


def InitPath():
    sys.path.remove(os.path.dirname(os.path.abspath(__file__)))
    # server path
    szServerPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, szServerPath)
    # common path
    szCommonPath = "".join((os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), os.path.sep, "common"))
    sys.path.insert(1, szCommonPath)


def main():
    print 1111111, sys.argv, "run_gas"

    InitPath()

    import gs.gs as gs
    app = gs.GameServer()
    app.Init()
    app.Run()

    from common_define import print_str
    print_str("按任意键结束")
    msvcrt.getch()

if __name__ == "__main__":
    main()

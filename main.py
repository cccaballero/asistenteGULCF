#!/bin/env python3
import locale
from remainder import should_notify


def run():
    try:
        locale.setlocale(locale.LC_TIME, "es_CU")
    except:
        locale.setlocale(locale.LC_TIME, "")
    should_notify()

if __name__ == '__main__':
    run()
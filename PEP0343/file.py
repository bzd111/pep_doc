# coding=utf-8
from __future__ import absolute_import
from . import contextmanager



@contextmanager
def opening(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


if __name__ == '__main__':
    with opening('1.txt') as f:
        f.write('Hello1, World')
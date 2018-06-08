# coding:utf-8
import sys


from . import contextmanager


@contextmanager
def stdout_redirected(new_stdout):
    save_stdout = sys.stdout
    sys.stdout = new_stdout
    try:
        yield None
    finally:
        sys.stdout = save_stdout


if __name__ == '__main__':
    with open('2.txt', 'w') as f:
        with stdout_redirected(f):
            print('Hello')
            print('world')
# coding:utf-8
from threading import Lock


from . import contextmanager

@contextmanager
def locked(lock):
    lock.acquire()
    try:
        yield
    finally:
        lock.release()


if __name__ == '__main__':
    with locked(Lock()):...

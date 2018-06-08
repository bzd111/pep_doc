# coding=utf-8
import sys


class GeneratorContextManager:

   def __init__(self, gen):
       self.gen = gen

   def __enter__(self):
       try:
           return self.gen.__next__()
       except StopIteration:
           raise RuntimeError("generator didn't yield")

   def __exit__(self, type, value, traceback):
       if type is None:
           try:
               self.gen.__next__()()
           except StopIteration:
               return
           else:
               raise RuntimeError("generator didn't stop")
       else:
           try:
               self.gen.throw(type, value, traceback)
               raise RuntimeError("generator didn't stop after throw()")
           except StopIteration:
               return True
           except:
               if sys.exc_info()[1] is not value:
                   raise


def contextmanager(func):
   def helper(*args, **kwds):
       return GeneratorContextManager(func(*args, **kwds))
   return helper



if __name__ == '__main__':
    pass
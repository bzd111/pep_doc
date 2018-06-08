# with语法糖
主要是靠两个魔法方法: `__enter__`、`__exit__`,
分别在进入和离开with语句的主体时被调用。

## 实现方法
1.**在类中实现这两个方法**

2.**使用contextmanager装饰器**

## 可使用对象
- file
- thread.LockType
- threading.Lock
- threading.RLock
- threading.Condition
- threading.Semaphore
- threading.BoundedSemaphore

## 运行方式
`python3 -m test.file`
# coding=utf-8
from . import contextmanager


@contextmanager
def transaction(db):
    db.begin()
    try:
        yield None
    except:
        db.rollback()
        raise
    else:
        db.commit()


if __name__ == '__main__':
    pass
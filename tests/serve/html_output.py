from dataflows import Flow
import logging


class MyClass():
    pass


def flow(*_):
    logging.info(f'my_object={str(MyClass())}')
    return Flow()

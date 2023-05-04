# pylama:skip=1
from typing import NamedTuple


class SpecError(NamedTuple):
    short_msg: str
    long_msg: str

    def __str__(self):
        return f'{self.short_msg}: {self.long_msg}'

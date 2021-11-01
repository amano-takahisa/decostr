#!/usr/bin/env python
from __future__ import annotations
from typing import Union

ESC = '\033'


class DecoStr(str):
    def __new__(cls, value: str) -> DecoStr:
        self = super(DecoStr, cls).__new__(cls, value)
        self.decostring = value
        self._str = value
        return self

    def __repr__(self) -> str:
        return self.decostring

    def __str__(self) -> str:
        return self.decostring

    def __add__(self, other: Union[str, DecoStr]) -> DecoStr:
        if isinstance(other, str):
            out = DecoStr(self.decostring + other)
            out._str = self.raw + other
        elif isinstance(other, DecoStr):
            out = DecoStr(self.decostring + other.decostring)
            out._str = self.raw + other.raw
        else:
            raise TypeError(f'type other {type(other)} is not supported.')
        return out

    def __radd__(self, other: Union[str, DecoStr]) -> DecoStr:
        if isinstance(other, str):
            out = DecoStr(other + self.decostring)
            out._str = other + self.raw
        elif isinstance(other, DecoStr):
            out = DecoStr(other.decostring + self.decostring)
            out._str = other.decostring + self.raw
        else:
            raise TypeError(f'type other {type(other)} is not supported.')
        return out

    def bold(self) -> DecoStr:
        self.decostring = f'{ESC}[1m{self.decostring}{ESC}[21m'
        return self

    def underline(self) -> DecoStr:
        self.decostring = f'{ESC}[4m{self.decostring}{ESC}[24m'
        return self

    @property
    def raw(self) -> str:
        return self._str

    @raw.setter
    def raw(self, value: str) -> None:
        self._str = value

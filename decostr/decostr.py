#!/usr/bin/env python
from __future__ import annotations
from typing import Union

ESC = '\033'

attribute_codes = {
    # https://en.wikipedia.org/wiki/ANSI_escape_code
    'bold': (1, 21),
    'dim': (2, 22),
    'italic': (3, 23),
    'underline': (4, 24),
    'blink': (5, 25),
    'blinkrapid': (6, 25),
    'invert': (7, 27),
    'hide': (8, 28),
    'strike': (9, 29)
}


def enclose(string: str, tag_type: str) -> str:
    open_tag = f'{ESC}[{attribute_codes[tag_type][0]}m'
    close_tag = f'{ESC}[{attribute_codes[tag_type][1]}m'
    return open_tag + string + close_tag


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
        self.decostring = enclose(string=self.decostring, tag_type='bold')
        return self

    def dim(self) -> DecoStr:
        self.decostring = enclose(string=self.decostring, tag_type='dim')
        return self

    def italic(self) -> DecoStr:
        self.decostring = enclose(string=self.decostring, tag_type='italic')
        return self

    def underline(self) -> DecoStr:
        self.decostring = enclose(string=self.decostring, tag_type='underline')
        return self

    def blink(self) -> DecoStr:
        self.decostring = enclose(string=self.decostring, tag_type='blink')
        return self

    def blinkrapid(self) -> DecoStr:
        self.decostring = enclose(string=self.decostring, tag_type='blinkrapid')
        return self

    def invert(self) -> DecoStr:
        self.decostring = enclose(string=self.decostring, tag_type='invert')
        return self

    def hide(self) -> DecoStr:
        self.decostring = enclose(string=self.decostring, tag_type='hide')
        return self

    def strike(self) -> DecoStr:
        self.decostring = enclose(string=self.decostring, tag_type='strike')
        return self

    @property
    def raw(self) -> str:
        return self._str

    @raw.setter
    def raw(self, value: str) -> None:
        self._str = value

#!/usr/bin/env python
from __future__ import annotations
from typing import Dict, Optional, Tuple, Union

ESC = '\033'

# https://en.wikipedia.org/wiki/ANSI_escape_code

attributes = {
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

fgcolors = {
    'black': (30, 39),
    'red': (31, 39),
    'green': (32, 39),
    'yellow': (33, 39),
    'blue': (34, 39),
    'magenta': (35, 39),
    'cyan': (36, 39),
    'white': (37, 39),
    'gray': (90, 39),
    'bright red': (91, 39),
    'bright green': (92, 39),
    'bright yellow': (93, 39),
    'bright blue': (94, 39),
    'bright magenta': (95, 39),
    'bright cyan': (96, 39),
    'bright white': (97, 39)
}

bgcolors = {
    'black': (40, 49),
    'red': (41, 49),
    'green': (42, 49),
    'yellow': (43, 49),
    'blue': (44, 49),
    'magenta': (45, 49),
    'cyan': (46, 49),
    'white': (47, 49),
    'gray': (100, 49),
    'bright red': (101, 49),
    'bright green': (102, 49),
    'bright yellow': (103, 49),
    'bright blue': (104, 49),
    'bright magenta': (105, 49),
    'bright cyan': (106, 49),
    'bright white': (107, 49)
}


def enclose_attributes(string: str,
                       code_dict: Dict[str, Tuple[int, int]],
                       item: str) -> str:
    open_tag = f'{ESC}[{code_dict[item][0]}m'
    close_tag = f'{ESC}[{code_dict[item][1]}m'
    return open_tag + string + close_tag


class DecoStr(str):
    def __new__(cls, value: Union[str, DecoStr]) -> DecoStr:
        self = super(DecoStr, cls).__new__(cls, value)
        if isinstance(value, DecoStr):
            self.decostring = value.decostring
            self._str = value.raw
        elif isinstance(value, str):
            self.decostring = value
            self._str = value
        return self

    def __repr__(self) -> str:
        return self.decostring

    def __str__(self) -> str:
        return self.decostring

    def __add__(self, other: Union[str, DecoStr]) -> DecoStr:
        if isinstance(other, DecoStr):
            out = DecoStr(self.decostring + other.decostring)
            out._str = self.raw + other.raw
        elif isinstance(other, str):
            out = DecoStr(self.decostring + other)
            out._str = self.raw + other
        else:
            raise TypeError(f'type other {type(other)} is not supported.')
        return out

    def __radd__(self, other: Union[str, DecoStr]) -> DecoStr:
        if isinstance(other, DecoStr):
            out = DecoStr(other.decostring + self.decostring)
            out._str = other.decostring + self.raw
        elif isinstance(other, str):  # noqa: E721
            out = DecoStr(other + self.decostring)
            out._str = other + self.raw
        else:
            raise TypeError(f'type other {type(other)} is not supported.')
        return out

    def bold(self) -> DecoStr:
        self.decostring = enclose_attributes(
            string=self.decostring, code_dict=attributes, item='bold')
        return self

    def dim(self) -> DecoStr:
        self.decostring = enclose_attributes(
            string=self.decostring, code_dict=attributes, item='dim')
        return self

    def italic(self) -> DecoStr:
        self.decostring = enclose_attributes(
            string=self.decostring, code_dict=attributes, item='italic')
        return self

    def underline(self) -> DecoStr:
        self.decostring = enclose_attributes(
            string=self.decostring, code_dict=attributes, item='underline')
        return self

    def blink(self) -> DecoStr:
        self.decostring = enclose_attributes(
            string=self.decostring, code_dict=attributes, item='blink')
        return self

    def blinkrapid(self) -> DecoStr:
        self.decostring = enclose_attributes(
            string=self.decostring, code_dict=attributes, item='blinkrapid')
        return self

    def invert(self) -> DecoStr:
        self.decostring = enclose_attributes(
            string=self.decostring, code_dict=attributes, item='invert')
        return self

    def hide(self) -> DecoStr:
        self.decostring = enclose_attributes(
            string=self.decostring, code_dict=attributes, item='hide')
        return self

    def strike(self) -> DecoStr:
        self.decostring = enclose_attributes(
            string=self.decostring, code_dict=attributes, item='strike')
        return self

    def color(self,
              color: Optional[str] = None,
              bgcolor: Optional[str] = None) -> DecoStr:
        if color:
            self.decostring = enclose_attributes(
                string=self.decostring, code_dict=fgcolors, item=color)
        if bgcolor:
            self.decostring = enclose_attributes(
                string=self.decostring, code_dict=bgcolors, item=bgcolor)
        return self

    @property
    def raw(self) -> str:
        return self._str

    @raw.setter
    def raw(self, value: str) -> None:
        self._str = value

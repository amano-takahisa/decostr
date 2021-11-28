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


class TagStr(str):
    def __new__(cls, value: Union[str, TagStr]) -> TagStr:
        self = super(TagStr, cls).__new__(cls, value)
        if isinstance(value, TagStr):
            self.tagstring = value.tagstring
            self._raw = value.raw
        elif isinstance(value, str):
            self.tagstring = value
            self._raw = value
        return self

    def __repr__(self) -> str:
        return self.tagstring

    def __str__(self) -> str:
        return self.tagstring

    def __add__(self, other: Union[str, TagStr]) -> TagStr:
        if isinstance(other, TagStr):
            out = TagStr(self.tagstring + other.tagstring)
            out._raw = self.raw + other.raw
        elif isinstance(other, str):
            out = TagStr(self.tagstring + other)
            out._raw = self.raw + other
        else:
            raise TypeError(f'type other {type(other)} is not supported.')
        return out

    def __radd__(self, other: Union[str, TagStr]) -> TagStr:
        if isinstance(other, TagStr):
            out = TagStr(other.tagstring + self.tagstring)
            out._raw = other.tagstring + self.raw
        elif isinstance(other, str):  # noqa: E721
            out = TagStr(other + self.tagstring)
            out._raw = other + self.raw
        else:
            raise TypeError(f'type other {type(other)} is not supported.')
        return out

    def bold(self) -> TagStr:
        tagstring = enclose_attributes(
            string=self.tagstring, code_dict=attributes, item='bold')
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    def dim(self) -> TagStr:
        tagstring = enclose_attributes(
            string=self.tagstring, code_dict=attributes, item='dim')
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    def italic(self) -> TagStr:
        tagstring = enclose_attributes(
            string=self.tagstring, code_dict=attributes, item='italic')
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    def underline(self) -> TagStr:
        tagstring = enclose_attributes(
            string=self.tagstring, code_dict=attributes, item='underline')
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    def blink(self) -> TagStr:
        tagstring = enclose_attributes(
            string=self.tagstring, code_dict=attributes, item='blink')
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    def blinkrapid(self) -> TagStr:
        tagstring = enclose_attributes(
            string=self.tagstring, code_dict=attributes, item='blinkrapid')
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    def invert(self) -> TagStr:
        tagstring = enclose_attributes(
            string=self.tagstring, code_dict=attributes, item='invert')
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    def hide(self) -> TagStr:
        tagstring = enclose_attributes(
            string=self.tagstring, code_dict=attributes, item='hide')
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    def strike(self) -> TagStr:
        tagstring = enclose_attributes(
            string=self.tagstring, code_dict=attributes, item='strike')
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    def color(self,
              color: Optional[str] = None,
              bgcolor: Optional[str] = None) -> TagStr:
        tagstring = self.tagstring
        if color:
            tagstring = enclose_attributes(
                string=tagstring, code_dict=fgcolors, item=color)
        if bgcolor:
            tagstring = enclose_attributes(
                string=tagstring, code_dict=bgcolors, item=bgcolor)
        out = TagStr(tagstring)
        out._raw = self.raw
        return out

    @property
    def raw(self) -> str:
        return self._raw

    @raw.setter
    def raw(self, value: str) -> None:
        self._raw = value

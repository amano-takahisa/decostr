#!/usr/bin/env python
from __future__ import annotations

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

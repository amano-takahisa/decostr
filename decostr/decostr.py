#!/usr/bin/env python

ESC = '\033'


class DecoStr(str):
    def __new__(cls, value):
        self = super(DecoStr, cls).__new__(cls, value)
        self.decostring = value
        self._str = value
        return self

    def __repr__(self):
        return self.decostring

    def __str__(self):
        return self.decostring

    def bold(self):
        self.decostring = f'{ESC}[1m{self.decostring}{ESC}[21m'
        return self

    def underline(self):
        self.decostring = f'{ESC}[4m{self.decostring}{ESC}[24m'
        return self

    @property
    def str(self):
        return self._str

    @str.setter
    def str(self, value):
        self._str = value


#!/usr/bin/env python

ESC = '\033'


class DecoStr(str):
    def __new__(cls, value):
        self = super(DecoStr, cls).__new__(cls, value)
        self.decostring = value
        return self

    def bold(self):
        self.decostring = f'{ESC}[1m{self.decostring}{ESC}[21m'
        return self

    def underline(self):
        self.decostring = f'{ESC}[4m{self.decostring}{ESC}[24m'
        return self

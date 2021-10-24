#!/usr/bin/env python

ESC = '\033'


class DecoStr:
    def __init__(self, string: str):
        self.string = string
        self.decostring = string

    def bold(self):
        self.decostring = f'{ESC}[1m{self.decostring}{ESC}[21m'
        return self

    def underline(self):
        self.decostring = f'{ESC}[4m{self.decostring}{ESC}[24m'
        return self

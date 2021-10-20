#!/usr/bin/env python

ESC = '\033'


class DecoStr:
    def __init__(self, string: str):
        self.string = string

    def bold(self):
        self.string = f'{ESC}[1m{self.string}{ESC}[21m'
        return self

    def underline(self):
        self.string = f'{ESC}[4m{self.string}{ESC}[24m'
        return self

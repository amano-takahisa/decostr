#!/usr/bin/env python

"""Tests for `decostr` package."""

import pytest


from decostr.decostr import DecoStr


class Test_DecoStr:
    def test_decostr(self):
        out = DecoStr('sample text').bold().underline()
        assert out.decostring == '\x1b[4m\x1b[1msample text\x1b[21m\x1b[24m'
        assert out == 'sample text'
        assert isinstance(out, str)
        assert isinstance(out, DecoStr)

    def test_str(self):
        out = DecoStr('sample text').bold().underline().str
        assert out == 'sample text'
        assert type(out) == str

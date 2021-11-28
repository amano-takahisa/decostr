#!/usr/bin/env python

"""Tests for `tagstr` package."""

import pytest


from tagstr.tagstr import TagStr


class Test_TagStr:
    def test_tagstr(self):
        out = TagStr('sample text').bold().underline()
        assert out.tagstring == '\x1b[4m\x1b[1msample text\x1b[21m\x1b[24m'
        assert out.raw == 'sample text'
        assert isinstance(out, str)
        assert isinstance(out, TagStr)

    def test_raw(self):
        out = TagStr('sample text').bold().underline().raw
        assert out == 'sample text'
        assert type(out) == str

    def test_add(self):
        out = TagStr('bold').bold() + ' normal'
        assert out.raw == 'bold normal'
        assert out.tagstring == '\x1b[1mbold\x1b[21m normal'

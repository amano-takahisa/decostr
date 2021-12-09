#!/usr/bin/env python

"""Tests for `tagstr` package."""

import pytest


from tagstr.tagstr import TagStr


class Test_TagStr:
    def test_tagstr(self):
        out = TagStr('sample text').bold().underline()
        assert out.tagged_text() == '\x1b[4m\x1b[1msample text\x1b[21m\x1b[24m'
        assert out.contents == 'sample text'
        assert isinstance(out, TagStr)


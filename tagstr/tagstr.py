#!/usr/bin/env python
from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Tuple, Union

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


class TagStr:
    def __init__(self,
                 contents: Union[str, TagStr],
                 tags: Dict[str, Union[bool, str, dict]] = {},
                 tagset: Literal['bash'] = 'bash'):
        self.contents = contents
        self.tags = tags
        self.tagset = tagset

    def _append_tag_to_copy(self,
                            tag: Dict[str, Union[bool, str, dict]]):
        tags = self.tags.copy()
        tags.update(tag)
        return TagStr(contents=self.contents,
                      tags=tags,
                      tagset=self.tagset)  # type: ignore

    def bold(self, tag: bool = True, /) -> TagStr:
        return self._append_tag_to_copy(tag={'bold': tag})

    def dim(self, tag: bool = True, /) -> TagStr:
        return self._append_tag_to_copy(tag={'dim': True})

    def italic(self, tag: bool = True, /) -> TagStr:
        return self._append_tag_to_copy(tag={'italic': tag})

    def underline(self, tag: bool = True, /) -> TagStr:
        return self._append_tag_to_copy(tag={'underline': tag})

    def blink(self, tag: bool = True, /) -> TagStr:
        return self._append_tag_to_copy(tag={'blink': tag})

    def blinkrapid(self, tag: bool = True, /) -> TagStr:
        return self._append_tag_to_copy(tag={'blinkrapid': tag})

    def invert(self, tag: bool = True, /) -> TagStr:
        return self._append_tag_to_copy(tag={'invert': tag})

    def hide(self, tag: bool = True, /) -> TagStr:
        return self._append_tag_to_copy(tag={'hide': tag})

    def strike(self, tag: bool = True, /) -> TagStr:
        return self._append_tag_to_copy(tag={'strike': tag})

    def color(self,
              fgcolor: Optional[str] = None,
              bgcolor: Optional[str] = None) -> TagStr:
        color = {}
        if fgcolor:
            color['fgcolor'] = fgcolor
        if bgcolor:
            color['bgcolor'] = bgcolor
        return self._append_tag_to_copy(tag={'color': color})

    def tagged_text(self) -> str:
        if self.tagset == 'bash':
            open_tag, close_tag = generate_bash_tags(self.tags)
        return open_tag + self.contents + close_tag


def generate_bash_tags(
        tags: Dict[str, Union[bool, str, dict]]) -> Tuple[str, str]:
    open_tag = close_tag = ''
    for tag_name, tag_value in tags.items():
        if (tag_name in attributes) and tag_value:
            open_tag = f'{ESC}[{attributes[tag_name][0]}m' + open_tag
            close_tag = close_tag + f'{ESC}[{attributes[tag_name][1]}m'
        elif tag_name in ['color']:
            for target, color in tag_value.items():  # type: ignore
                if color:  # type: ignore
                    if target == 'fgcolor':
                        color_codes =fgcolors[color]
                    if target == 'bgcolor':
                        color_codes =bgcolors[color]
                    open_tag = f'{ESC}[{color_codes[0]}m' + open_tag
                    close_tag = close_tag + f'{ESC}[{color_codes[1]}m'
        else:
            raise NotImplementedError(f'tag {tag_name} is not implemented.')
    return open_tag, close_tag

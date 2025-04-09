# file: flutils/txtutils.py:181-211
# asked: {"lines": [181, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 194, 195, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211], "branches": []}
# gained: {"lines": [181, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 194, 195, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_default_initialization():
    wrapper = AnsiTextWrapper()
    assert wrapper.width == 70
    assert wrapper.initial_indent == ''
    assert wrapper.subsequent_indent == ''
    assert wrapper.expand_tabs is True
    assert wrapper.replace_whitespace is True
    assert wrapper.fix_sentence_endings is False
    assert wrapper.break_long_words is True
    assert wrapper.drop_whitespace is True
    assert wrapper.break_on_hyphens is True
    assert wrapper.tabsize == 8
    assert wrapper.max_lines is None
    assert wrapper.placeholder == ' [...]'

def test_ansi_text_wrapper_custom_initialization():
    wrapper = AnsiTextWrapper(
        width=50,
        initial_indent='* ',
        subsequent_indent='> ',
        expand_tabs=False,
        replace_whitespace=False,
        fix_sentence_endings=True,
        break_long_words=False,
        drop_whitespace=False,
        break_on_hyphens=False,
        tabsize=4,
        max_lines=2,
        placeholder='...'
    )
    assert wrapper.width == 50
    assert wrapper.initial_indent == '* '
    assert wrapper.subsequent_indent == '> '
    assert wrapper.expand_tabs is False
    assert wrapper.replace_whitespace is False
    assert wrapper.fix_sentence_endings is True
    assert wrapper.break_long_words is False
    assert wrapper.drop_whitespace is False
    assert wrapper.break_on_hyphens is False
    assert wrapper.tabsize == 4
    assert wrapper.max_lines == 2
    assert wrapper.placeholder == '...'

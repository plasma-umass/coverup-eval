# file flutils/txtutils.py:181-211
# lines [181, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 194, 195, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_initialization():
    wrapper = AnsiTextWrapper(
        width=80,
        initial_indent='>>',
        subsequent_indent='--',
        expand_tabs=False,
        replace_whitespace=False,
        fix_sentence_endings=True,
        break_long_words=False,
        drop_whitespace=False,
        break_on_hyphens=False,
        tabsize=4,
        max_lines=2,
        placeholder=' [more]'
    )

    assert wrapper.width == 80
    assert wrapper.initial_indent == '>>'
    assert wrapper.subsequent_indent == '--'
    assert wrapper.expand_tabs is False
    assert wrapper.replace_whitespace is False
    assert wrapper.fix_sentence_endings is True
    assert wrapper.break_long_words is False
    assert wrapper.drop_whitespace is False
    assert wrapper.break_on_hyphens is False
    assert wrapper.tabsize == 4
    assert wrapper.max_lines == 2
    assert wrapper.placeholder == ' [more]'

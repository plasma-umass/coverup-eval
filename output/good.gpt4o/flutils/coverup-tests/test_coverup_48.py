# file flutils/txtutils.py:59-108
# lines [59, 60]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper():
    # Test with default parameters
    wrapper = AnsiTextWrapper()
    text = "This is a sample text with ANSI codes \033[1mBold\033[0m and \033[4mUnderline\033[0m."
    wrapped_text = wrapper.wrap(text)
    assert isinstance(wrapped_text, list)
    assert len(wrapped_text) > 0

    # Test with custom parameters
    wrapper = AnsiTextWrapper(width=50, initial_indent='>> ', subsequent_indent='-- ')
    text = "This is a sample text with ANSI codes \033[1mBold\033[0m and \033[4mUnderline\033[0m."
    wrapped_text = wrapper.wrap(text)
    assert isinstance(wrapped_text, list)
    assert len(wrapped_text) > 0
    assert wrapped_text[0].startswith('>> ')
    if len(wrapped_text) > 1:
        assert wrapped_text[1].startswith('-- ')

    # Test with expand_tabs and replace_whitespace
    wrapper = AnsiTextWrapper(expand_tabs=True, replace_whitespace=True)
    text = "This\tis\ta\tsample\ttext\twith\tANSI\tcodes."
    wrapped_text = wrapper.wrap(text)
    assert isinstance(wrapped_text, list)
    assert len(wrapped_text) > 0
    assert '\t' not in ''.join(wrapped_text)

    # Test with fix_sentence_endings
    wrapper = AnsiTextWrapper(fix_sentence_endings=True)
    text = "This is a sentence. This is another sentence!"
    wrapped_text = wrapper.wrap(text)
    assert isinstance(wrapped_text, list)
    assert len(wrapped_text) > 0
    assert '  ' in ''.join(wrapped_text)

    # Test with break_long_words
    wrapper = AnsiTextWrapper(break_long_words=False)
    text = "Thisisaverylongwordthatshouldnotbebroken."
    wrapped_text = wrapper.wrap(text)
    assert isinstance(wrapped_text, list)
    assert len(wrapped_text) == 1
    assert wrapped_text[0] == text

    # Test with drop_whitespace
    wrapper = AnsiTextWrapper(drop_whitespace=True)
    text = "This is a sample text with trailing whitespace    "
    wrapped_text = wrapper.wrap(text)
    assert isinstance(wrapped_text, list)
    assert len(wrapped_text) > 0
    assert wrapped_text[-1].rstrip() == wrapped_text[-1]

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Cleanup code to ensure no side effects
    yield
    mocker.stopall()

# file flutils/txtutils.py:59-108
# lines [59, 60]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

@pytest.fixture
def clean_ansi_text_wrapper():
    # Setup
    wrapper = AnsiTextWrapper()
    yield wrapper
    # Teardown
    # No cleanup needed as the wrapper is a local object and will be garbage collected

def test_ansi_text_wrapper_break_long_words_false(clean_ansi_text_wrapper):
    text = "ThisIsAVeryLongWordThatExceedsTheWidthLimit"
    clean_ansi_text_wrapper.width = 10
    clean_ansi_text_wrapper.break_long_words = False
    wrapped_text = clean_ansi_text_wrapper.wrap(text)
    assert wrapped_text == [text], "Long word should not be broken"

def test_ansi_text_wrapper_fix_sentence_endings_true(clean_ansi_text_wrapper):
    text = "This is a sentence. Followed by another sentence."
    clean_ansi_text_wrapper.width = 30
    clean_ansi_text_wrapper.fix_sentence_endings = True
    wrapped_text = clean_ansi_text_wrapper.wrap(text)
    assert wrapped_text == ["This is a sentence.  Followed", "by another sentence."], "Sentences should be separated by two spaces"

def test_ansi_text_wrapper_drop_whitespace_false(clean_ansi_text_wrapper):
    text = "This is a line with     excessive whitespace."
    clean_ansi_text_wrapper.width = 30
    clean_ansi_text_wrapper.drop_whitespace = False
    wrapped_text = clean_ansi_text_wrapper.wrap(text)
    assert wrapped_text == ["This is a line with     ", "excessive whitespace."], "Whitespace should not be dropped"

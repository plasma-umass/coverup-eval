# file tornado/locale.py:176-216
# lines [203, 205]
# branches ['202->203', '204->205']

import os
import gettext
import pytest
from unittest import mock
from tornado.locale import load_gettext_translations

@pytest.fixture
def mock_log(mocker):
    return mocker.patch("tornado.locale.gen_log")

@pytest.fixture
def temp_translation_dir(tmp_path):
    # Create a temporary directory structure for translations
    directory = tmp_path / "locale"
    directory.mkdir()
    (directory / ".svn").mkdir()  # Hidden directory to trigger line 203
    (directory / "file.txt").touch()  # File to trigger line 205
    yield directory

def test_load_gettext_translations_skips_hidden_and_files(temp_translation_dir, mock_log):
    from tornado.locale import _translations, _supported_locales, _use_gettext

    load_gettext_translations(str(temp_translation_dir), "domain")

    # Ensure that the hidden directory and file are skipped
    assert ".svn" not in _translations
    assert "file.txt" not in _translations

    # Ensure that the log does not contain errors for the skipped entries
    mock_log.error.assert_not_called()

    # Clean up global variables to avoid side effects on other tests
    _translations.clear()
    _supported_locales = frozenset()
    _use_gettext = False

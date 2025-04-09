# file tornado/locale.py:176-216
# lines [176, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 211, 212, 213, 214, 215, 216]
# branches ['201->202', '201->214', '202->203', '202->204', '204->205', '204->206']

import os
import gettext
import pytest
from unittest import mock
from tornado import locale
from tornado.log import gen_log

@pytest.fixture
def mock_log(mocker):
    return mocker.patch.object(gen_log, 'error'), mocker.patch.object(gen_log, 'debug')

@pytest.fixture
def temp_translation_dir(tmp_path):
    directory = tmp_path / "locale"
    directory.mkdir()
    (directory / "en" / "LC_MESSAGES").mkdir(parents=True)
    (directory / "es" / "LC_MESSAGES").mkdir(parents=True)
    (directory / "fr" / "LC_MESSAGES").mkdir(parents=True)
    (directory / "en" / "LC_MESSAGES" / "test.mo").write_text("dummy content")
    (directory / "es" / "LC_MESSAGES" / "test.mo").write_text("dummy content")
    return directory

def test_load_gettext_translations(temp_translation_dir, mock_log):
    error_log, debug_log = mock_log

    # Mock gettext.translation to avoid actual file parsing
    with mock.patch('gettext.translation', return_value=mock.Mock()):
        locale.load_gettext_translations(str(temp_translation_dir), "test")
    
    assert "en" in locale._translations
    assert "es" in locale._translations
    assert "fr" not in locale._translations
    assert locale._use_gettext is True
    assert debug_log.call_count == 1
    assert error_log.call_count == 1
    error_log.assert_called_with("Cannot load translation for '%s': %s", "fr", mock.ANY)
    debug_log.assert_called_with("Supported locales: %s", sorted(locale._supported_locales))

    # Clean up
    locale._translations = {}
    locale._supported_locales = frozenset()
    locale._use_gettext = False
